# flake8: noqa
import sys
sys.setrecursionlimit(20000)

# FUNCIONES RECURSIVAS EMPIEZAN AQUI

def merge(left, right):
    merged_list = []
    # SU SOLUCION EMPIEZA AQUI
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
    merged_list.extend(left[i:])
    merged_list.extend(right[j:])
    # SU SOLUCION TERMINA AQUI
    return merged_list

def merge_sort(lista):
    # SU SOLUCION EMPIEZA AQUI
    length = len(lista)
    if length <= 1:
        return lista
    mid = length // 2
    left = merge_sort(lista[:mid])
    right = merge_sort(lista[mid:])
    # SU SOLUCION TERMINA AQUI
    return merge(left, right)

# FUNCIONES RECURSIVAS TERMINAN AQUI

class Solution:

    # NO MODIFICAR ABAJO DE ESTÁ LINEA, ES PARTE DEL AUTOGRADER
    def sort(self, data=[]):
        return "clear"

    def sorted(self, data=[]):
        return "clear"
    # NO MODIFICAR ARRIBA DE ESTÁ LINEA, ES PARTE DEL AUTOGRADER

    # ============ Pregunta  1============

    def crear_diccionarios(self, ruta="pokemon.csv"):
        pokemones = {}
        # SU SOLUCION EMPIEZA AQUI
        with open(ruta, "r") as f:
            next(f)
            for linea in f:
                linea = linea.replace("\n", "").split(";")
                name, id_, attack, defense, speed, ability = linea
                pokemones[int(id_)] = {
                    "nombre": name,
                    "puntos_ataque": int(attack),
                    "puntos_defensa": int(defense),
                    "puntos_velocidad": int(speed),
                    "habilidad": ability,
                }
        # SU SOLUCION TERMINA AQUI
        return pokemones

    # ============ Pregunta  2============
    def buscar_dato_pokemon(self, pokemones, id, valor):
        result = ""
        # SU SOLUCION EMPIEZA AQUI
        try:
            result = pokemones[id][valor]
        except KeyError:
            result = "Pokémon no encontrado"
        # SU SOLUCION TERMINA AQUI
        return result

    # ============ Pregunta 3============
    def pokemon_rapido(self, pokemones):
        result = ()
        # SU SOLUCION EMPIEZA AQUI
        max_ = 0
        for v in pokemones.values():
            if v["puntos_velocidad"] > max_:
                max_ = v["puntos_velocidad"]
                result = v["nombre"], max_
        # SU SOLUCION TERMINA AQUI
        return result

    # ============ Pregunta 4============
    def nombre_ascendente(self, pokemones):
        result = []
        # SU SOLUCION EMPIEZA AQUI
        for id_, v in pokemones.items():
            result.append((v["nombre"], id_))
        result = merge_sort(result)
        # SU SOLUCION TERMINA AQUI
        return result

    # ============ Pregunta 5============
    def busqueda_habilidad(self, nombre_a_buscar, nombres_ordenados, pokemones):
        result = {}
        # SU SOLUCION EMPIEZA AQUI
        def binary_search(arr, x):
            low = 0
            high = len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid][0] == x:
                    return mid
                elif arr[mid][0] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        index = binary_search(nombres_ordenados, nombre_a_buscar)
        if index != -1:
            id_ = nombres_ordenados[index][1]
            result = {id_: pokemones[id_]}
        else:
            result = {-1: "No encontrado"}
        # SU SOLUCION TERMINA AQUI
        return result
