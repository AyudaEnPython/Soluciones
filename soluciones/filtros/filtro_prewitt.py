"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import cv2
import numpy as np


def filtro_prewitt(img, k_size=3):
    H, W = img.shape
    pad = k_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2), dtype=float)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(float)
    t = out.copy()
    out_v = out.copy()
    out_h = out.copy()
    v_k = [[-1., -1., -1.], [ 0., 0., 0.], [ 1., 1., 1.]]
    h_k = [[-1.,  0.,  1.], [-1., 0., 1.], [-1., 0., 1.]]
    for y in range(H):
        for x in range(W):
            out_v[pad + y, pad + x] = np.sum(v_k * (t[y: y + k_size, x: x + k_size]))
            out_h[pad + y, pad + x] = np.sum(h_k * (t[y: y + k_size, x: x + k_size]))
    out_v = np.clip(out_v, 0, 255)
    out_h = np.clip(out_h, 0, 255)
    out_v = out_v[pad: pad + H, pad: pad + W].astype(np.uint8)
    out_h = out_h[pad: pad + H, pad: pad + W].astype(np.uint8)
    return out_v, out_h


img = cv2.imread("assets/logo.png",0).astype(float)
out_v, out_h = filtro_prewitt(img, k_size=3)
cv2.imwrite("out_v.jpg", out_v)
cv2.imshow("result_v", out_v)
cv2.imwrite("out_h.jpg", out_h)
cv2.imshow("result_h", out_h)
cv2.waitKey(0)
cv2.destroyAllWindows()