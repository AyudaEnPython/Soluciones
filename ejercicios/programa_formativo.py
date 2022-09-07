"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Tu labor en esta ocasión es ayudar a Eren Jaeger. Para ello, debes
determinar por él si ha aprobado el Programa Formativo como soldado
o no para poder formar parte de la Legión de Reconocimiento. La única
forma de aprobar dicho programa es aprobando todos y cada uno de los N
cursos que lo componen.

- Cada curso está compuesto por Mi notas donde i va de 1 a N.
- No necesariamente todos los cursos tiene la misma cantidad de notas.
- Cada curso está identificado por un código único diferente.
    - En caso el código del cruso sea par, será necesario que el
        promedio de las notas de dicho curso sea mayor o igual a 11.
    - En caso el código del curso sea impar, la única forma de aprobar
        es obtener al menos una nota que sea mayor o igual al 16.

Parámetros del programa
1. El numero entero N que representa la cantidad de cursos.
2. Una lista de codigos de longuitud N que representa los codigos de los
    cursos.
3. Una lista M de longuitud N donde cada elemento Mi representa la
    cantidad de notas del curso con el código en la misma posición i.
4. Una matriz notas de tamaño NxMi que representa todas las notas de
    Eren.
5. Recuerde que usted debe usar los parámetros de las funciones, no
    debe adicionar inputs.

Entrega de resultados
1. Si N es un numero menor o igual a 0. Usted deberá retornar "Código
    de autodestrucción detectado. Iniciando proceso en 3, 2, 1" y no
    ejecutará la lógica del cálculo de notas.
2. Si cualquier Mi cantidad de notas es un numero menor o igual a 0.
    Usted deberá retornar "Error, no pueden existir cursos sin notas" y
    no ejecutará la lógica del cálculo de notas.
3. En el caso de aprobar el Programa Formatico como soldado, usted debe
    retornar "Felicitaciones. Te graduaste".
4. De lo contrario, debe retornar "Has reprobado. Pero no te rindas,
    toma el Programa nuevamente. Aprobaste X de los N cursos". Donde X
    es la cantidad de cursos aprobados por Eren y N es el total de
    cursos que fue indicado al inicio por Eren.
5. En caso se inserten 2 códigos de curso iguales, se debe retornar
    "Error, ha introducido el mismo curso 2 veces" y no se ejecutará la
    lógica del cálculo de notas.

Usted solo debe retornar un único mensaje de error, en el caso de que
usted detecte múltiples errores diferentes al mismo tiempo, su programa
debe retornar el error con menor índice según la numeración presentada
anteriormente (números más pequeños simboliza mayor prioridad). Por
ejemplo, si usted detecta error de la regla 1, pero a la vez el error
de la regla 5, solo debe retornar el mensaje "Código de autodestrucción
detectado. Iniciando proceso en 3, 2, 1." Tenga en cuenta que las
únicas reglas consideradas como error son 1, 2 y 5.

Ejemplo 1:
Parámetros:
N = 3
codigos = [10001, 10002, 99991],
M = [2, 3, 1],
notas = [[16, 9], [1, 20, 15], [20]]

Retorno:
Felicitaciones. Te graduaste.

Explicación: Se debe evaluar curso por curso si se cumple la condición
    de acuerdo al tipo de código de curso que este tenga. Para el curso
'10001' se debe cumplir que tenga al menos una nota mayor o igual a 16,
lo cual es verdadero. De la misma manera ocurre con '99991'. En el caso
de '10002' se sacó el promedio y se verificó que cumple la condición
propuesta. Por lo que, al haber aprobado todos los cursos, Eren ha
logrado graduarse del Programa de Formación de soldados.

Ejemplo 2:
Parámetros:
N = 2
codigos = [10001, 10002],
M = [2, 3],
notas = [[15, 9], [1, 20, 15]]

Retorno:
Has reproba. Pero no te rindas, toma el Programa nuevamente. Aprobaste
1 de los 2 cursos
"""
from typing import List, Tuple
from unittest import main, TestCase
from statistics import mean

PROMEDIO_MINIMO = 11
NOTA_MINIMA_IMPAR = 16


def validar_numero(numero: int) -> bool:
    """Valida un numero si es positivo o negativo

    :param numero: Numero a validar
    :numero type: int
    :return: True si el numero es menor igual a cero, de lo contrario
        False
    :rtype: bool
    """
    return True if numero <= 0 else False


def validar_codigos(codigos: List[int]) -> bool:
    return True if len(codigos) != len(set(codigos)) else False


def _tipo_curso(codigo: int) -> bool:
    return True if codigo % 2 == 0 else False


def calcular(notas: List[int], codigos: List[int]) -> Tuple[bool, List[bool]]:
    resultado = []
    for codigo, curso in zip(codigos, notas):
        promedio = mean(curso)
        if _tipo_curso(codigo):
            resultado.append(True if promedio >= PROMEDIO_MINIMO else False)
        else:
            resultado.append(
                True if any(n >= NOTA_MINIMA_IMPAR for n in curso) else False
            )
    return all(resultado), resultado


def programa_formativo(
    N: int,
    codigos: List[int],
    M: List[int],
    notas: List[List[int]],
) -> str:
    """Determina si se aprobó o desaprobó el Programa Formativo.

    :param N: Cantidad de cursos
    :type N: int
    :param codigos: Códigos de los cursos.
    :type codigos: List(int)
    :param M: Cantidad de notas de los cursos con el código en la misma
        posición.
    :type M: List[int]
    :param notas: Representación de las notas (matriz)
    :type notas: List[List[int]]
    :return: Mensaje indicando si aprobo o desaprobo. Si desaprueba, se
        muestra la cantidad de cursos que se aprobo. Si existe un error
        en los datos, indica el error.
    :rtype: str
    """
    if validar_numero(N):
        return "Código de autodestrucción detectado." \
                " Iniciando proceso en 3, 2, 1."
    for m in M:
        if validar_numero(m):
            return "Error, no pueden existir cursos sin notas"
    if validar_codigos(codigos):
        return "Error, ha introducido el mismo curso 2 veces"
    estado, resultado = calcular(notas, codigos)
    if estado:
        return "Felicitaciones. Te graduaste"
    else:
        return (
            f"Has reprobado. Pero no te rindas, toma el Programa nuevamente."
            f" Aprobaste {sum(resultado)} de los {N} cursos."
        )


class Test(TestCase):

    data = (
        (
            3,
            [10001, 10002, 99991],
            [2, 3, 1],
            [[16, 9], [1, 20, 15], [20]],
        ),
        (
            2,
            [10001, 10002],
            [2, 3],
            [[15, 9], [1, 20, 15]],
        )
    )
    results = (
        "Felicitaciones. Te graduaste",
        "Has reprobado. Pero no te rindas, toma el Programa nuevamente."
        " Aprobaste 1 de los 2 cursos."
    )

    def test_validar_numero(self):
        self.assertEqual(validar_numero(-1), True)
        self.assertEqual(validar_numero(1), False)

    def test_validar_codigos(self):
        self.assertEqual(validar_codigos([1, 2, 1]), True)
        self.assertEqual(validar_codigos([1, 2, 3]), False)

    def test_tipo_codigo(self):
        self.assertEqual(_tipo_curso(2), True)
        self.assertEqual(_tipo_curso(3), False)

    def test_calcular(self):
        self.assertEqual(calcular([[1]], [2]), (False, [False]))
        self.assertEqual(calcular([[16, 11]], [1]), (True, [True]))

    def test_main(self):
        for data, result in zip(self.data, self.results):
            self.assertEqual(programa_formativo(*data), result)


if __name__ == "__main__":
    main()
