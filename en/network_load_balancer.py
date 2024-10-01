"""
# Network Load Balancer

A company’s website experiences varying levels of traffic throughout the day.
To ensure efficient handling of requests and maintain uptime, they need a
dynamic load balancer that can distribute the load across multiple servers.

Task: Develop an algorithm that simulates an adaptive load balancer capable
of handling fluctuating traffic patterns. The algorithm should distribute
incoming network requests to servers based on current load, server health,
and traffic type, ensuring efficient resource utilization and minimal
response time.

Input:
A list of servers, each with its processing power, current load, and health
status. A stream of incoming network requests, each with a required processing
time and priority level.

Output:
A real-time distribution plan for the requests across the servers, considering
the adaptive nature of traffic and server status.

Input Format
S N P1 L1 H1 C1 P2 L2 H2 C2 ... PS LS HS CS R1 T1 Pr1 R2 T2 Pr2 ... RN TN PrN

Where:
S is the number of servers.
N is the number of incoming network requests.

Pi is the processing power of the i-th server.
Li is the current load (as a percentage) of the i-th server.
Hi is the health status of the i-th server (1 for healthy, 0 for degraded).
Ci is the simultaneous request limit for the i-th server.

Ri is the ID of the i-th request.
Ti is the required processing time for the i-th request.
Pri is the priority level of the i-th request (1 for high, 2 for medium, 3 for low).

Constraints
Servers can process multiple requests simultaneously up to their capacity limit.
High-priority requests should be processed with a faster response time.
The load balancer must adapt to server health changes by redistributing the
load without service interruption.

Output Format
R1 S1 R2 S2 ... RN SN

Where:
Ri is the ID of the i-th request.
Si is the ID of the server assigned to handle the i-th request.

Sample Input 0
2 3
100 30 1 2
200 60 1 3
1 50 1
2 100 2
3 150 1

Sample Output 0
1 1
2 2
3 2
"""


def f(ss, rs):
    def g(s):
        p = s["pp"] / 100
        c = (1 - s["l"]/100) * s["c"]
        return p * c * s["h"]

    ss.sort(key=g, reverse=True)
    xs = []
    for r in rs:
        hs = [s for s in ss if s["h"] == 1]
        if r["p"] == 1:
            cs = hs[0]
        else:
            ml = min(s["l"] for s in hs)
            # cs = next(s for s in hs if s["cl"] == ml)
            cd = [s for s in hs if s["l"] == ml]
            cs = max(cd, key=lambda x: x["c"])
        cs["l"] += r["pt"]
        xs.append([r["ri"], cs["si"]])
    return xs


if __name__ == "__main__":
    ss = [
        {"pp": 100, "l": 30, "h": 1, "c": 2, "si": 1},
        {"pp": 200, "l": 60, "h": 1, "c": 3, "si": 2},
    ]
    rs = [
        {"ri": 1, "pt": 50, "p": 1},
        {"ri": 2, "pt": 100, "p": 2},
        {"ri": 3, "pt": 150, "p": 1},
    ]
    xs = f(ss.copy(), rs.copy())
    print(xs) # [[1, 2], [2, 1], [3, 2]]
