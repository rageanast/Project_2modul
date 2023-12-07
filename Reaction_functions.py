import chemlib
from chemlib import *
import math
from math import gcd
import numpy as np
import sympy
from sympy import Matrix, lcm
with open('Reference_data.txt', 'r') as file:
    spravochnik = file.read()
    exec(spravochnik) ##преобразование строки из файла в массив
def balance_equation(equation): ##уравнивание реакции
    elements = equation.split('-->')
    reagents = elements[0].split(' + ')
    products = elements[1].split(' + ')
    separate_elements=[]
    unique_elements=[]
    ind=0
    while ind<len(equation):
        if equation[ind] in "QWERTYUIOPASDFGHJKLZXCVBNM":
            if ind+1<len(equation):
                if equation[ind+1] in "qwertyuiopasdfghjklzxcvbnm":
                    if ind+2<len(equation):
                        if equation[ind+2] in "23456789":
                            separate_elements.append(equation[ind]+equation[ind+1]+equation[ind+2])
                            unique_elements.append(equation[ind]+equation[ind+1])
                            ind=ind+2
                        else:
                            separate_elements.append(equation[ind]+equation[ind+1])
                            unique_elements.append(equation[ind]+equation[ind+1])
                            ind=ind+1
                    else:
                        separate_elements.append(equation[ind]+equation[ind+1])
                        unique_elements.append(equation[ind]+equation[ind+1])
                        ind=ind+1
                elif equation[ind+1] in "23456789":
                    separate_elements.append(equation[ind]+equation[ind+1])
                    unique_elements.append(equation[ind])
                    ind=ind+1
                else:
                    separate_elements.append(equation[ind])
                    unique_elements.append(equation[ind])
            else:
                separate_elements.append(equation[ind])
                unique_elements.append(equation[ind])
        elif equation[ind] in "+>":
            separate_elements.append(equation[ind])
        elif equation[ind]=="(":
            separate_elements.append(equation[ind])
        elif equation[ind]==")":
            if equation[ind+1] in "23456789":
                separate_elements.append(equation[ind]+equation[ind+1])
                ind=ind+1
            else:
                separate_elements.append(equation[ind]+"1")
        ind=ind+1
    unique_elements=list(set(unique_elements))
    elems_data = []
    ind=0
    which_part="+"
    
    equation_parts=[which_part]
    paran_open=0
    while ind<len(separate_elements):
        if separate_elements[ind]=="+":
            elems_data.append(equation_parts)
            equation_parts=[which_part]
        elif separate_elements[ind]==">":
            elems_data.append(equation_parts)
            which_part="-"
            equation_parts=[which_part]
        elif separate_elements[ind]=="(":
            paran_open=1
        elif separate_elements[ind][0]==")":
            paran_open=0
            for e in range(1,len(equation_parts)):
                if equation_parts[e][1][-1]=="(":
                    equation_parts[e][1]=(equation_parts[e][1])[:-1]
                    equation_parts[e][1]=str(int(equation_parts[e][1])*int(separate_elements[ind][1]))
        else:
            if separate_elements[ind][-1] in "23456789":
                if paran_open==1:
                    el=[separate_elements[ind][:-1], separate_elements[ind][-1]+"("]
                else:
                    el=[separate_elements[ind][:-1], separate_elements[ind][-1]]
            else:
                if paran_open==1:
                    el=[separate_elements[ind], "1("]
                else:
                    el=[separate_elements[ind], "1"]
            equation_parts.append(el)
        ind=ind+1
    elems_data.append(equation_parts)
    
    math_system=[]
    for i in unique_elements:
        math_equasion=[]
        for j in range(len(elems_data)):
            flag=0
            for k in range(1,len(elems_data[j])):
                if i==elems_data[j][k][0]:
                    math_equasion.append(int(elems_data[j][0]+elems_data[j][k][1]))
                    flag=1
            if flag==0:
                math_equasion.append(0)
        math_system.append(math_equasion)
    
    A=Matrix(math_system)
    coefficients=A.nullspace()[0]
    m = lcm([val.q for val in coefficients])
    for i in range(len(coefficients)):
        coefficients[i]*=m
    balanced_equation = ''
    for index, coefficient in enumerate(coefficients):
        if index<len(reagents):
            balanced_equation += str(abs(int(coefficient))) + reagents[index].strip()+ ' + '
        else:
            break
    balanced_equation = balanced_equation[:-3] + '-->'
    for index, coefficient in enumerate(coefficients[len(reagents):]):
        balanced_equation += str(abs(int(coefficient))) + products[index].strip() + ' + '
    return balanced_equation[:-3]

def devision_into_parts(equation): ##делит левую часть уравнения по +
     reagents = equation.split(' + ')
     return reagents

def devision_into_elements(reagent): ##делит формулу на элементы
    elements = []
    current_element = ""
    
    i = 0
    while i < len(reagent):
        if reagent[i].isupper():
            if current_element != "":
                elements.append(current_element)
            current_element = reagent[i]
        elif reagent[i].islower():
            current_element += reagent[i]
        elif reagent[i].isdigit():
            if current_element:
                elements.append(current_element)
                current_element = ""
            j = i + 1
            coefficient = ""
            while j < len(reagent) and reagent[j].isdigit():
                coefficient += reagent[j]
                j += 1
            coefficient = int(coefficient) if coefficient else 1
            if elements:
                elements[-1] = elements[-1] * coefficient
        i += 1
    if current_element:
        elements.append(current_element)
    return elements

def devision_into_numbers(reagents): ##выделяет из формулы индексы
    numbers = []
    for element in reagents:
        if element.isdigit() and element not in numbers:
            numbers += element
    return numbers

def nod_two(element1, curr_nod=0): ##ищет НОД СО двух элементов
    element1 = abs(int(oxidation_states.get(element1)))
    while curr_nod:
        element1, curr_nod = curr_nod, element1%curr_nod
    return element1        
    
def find_nod(elements): ##ищет НОД нескольких элементов
    elements = devision_into_elements(elements)
    nod = abs(int(oxidation_states.get(elements[0])))
    for i in range(1, len(elements)):
        nod = nod_two(curr_nod=nod,element1=elements[i])
    return nod

def release_of_acid_residue(reagent): ##выделяет из формулы кислотный остаток
     a_oxide = ''
     i=0
     while (a_oxide not in acid_strengt) and (i<10) and (a_oxide[:-1] not in acid_strengt):
          reagent = reagent[1:]
          a_oxide = reagent
          i+=1
     if (a_oxide in acid_strengt):
          return a_oxide
     elif(a_oxide[:-1] in acid_strengt):
          return a_oxide[:-1]
     else:
          return("Error")

def release_of_metal(reagent): ##выделяет из формулы металл
     metal = ''
     i=0
     while (metal not in Me) and (i<10):
          reagent = reagent[:-1]
          metal = reagent
          i+=1
     return metal

def oxidation(equation, f = devision_into_parts): ##окисление (металл и неметалл)
    reagents = f(equation)
    elem0 = devision_into_elements(reagents[0])
    elem1 = devision_into_elements(reagents[1])
    str_elem0 = ', '.join(elem0)
    str_elem1 = ', '.join(elem1)
    if (str_elem0 in Me or str_elem1 in Me or str_elem0 in Ne_Me or str_elem1 in Ne_Me) and (reagents[0]=='O2' or reagents[1] =='O2'):
        if reagents[0] == 'O2':
            el = reagents[1]
            reagents[1] = reagents[0]
            reagents[0] = el
        if reagents[0] != 'N2' and reagents[0] != 'F2':
            nod = gcd(abs(int(oxidation_states.get(str_elem0))),abs(int(oxidation_states.get(str_elem1))))
            reaction = equation + '-->' + str_elem0+str(int(abs(int(oxidation_states.get(str_elem1))/nod))) + str_elem1  + str(int(abs(int(oxidation_states.get(str_elem0)))/nod))
            return balance_equation(reaction), 'горение'
        if reagents[0] == 'N2':
            reaction = equation + '-->' + 'NO'
            return balance_equation(reaction), 'горение'
        if reagents[0] == 'F2':
            reaction = equation + '-->' + 'OF2'
            return balance_equation(reaction), 'горение'

def combustion(equation, f = devision_into_parts): ##горение сложных элементов
    reagents = f(equation)
    if reagents[0] == 'O2' or reagents[1] == 'O2':
        if reagents[0] == 'O2':
            elem = reagents[1]
            reagents[1] = reagents[0]
            reagents[0] = elem
        if reagents[0] not in exceptions:
            if len(devision_into_elements(reagents[0]))==2:
                elems = devision_into_elements(reagents[0])
                elem_in_0 = devision_into_elements(reagents[0])
                nod_1 = int(gcd(abs(int(oxidation_states.get('O'))), abs(int(oxidation_states.get(elem_in_0[0])))))
                nod_2 = int(gcd(abs(int(oxidation_states.get('O'))), abs(int(oxidation_states.get(elem_in_0[1])))))
                product1 = (elem_in_0[0]+str(int((abs(int(oxidation_states.get('O')))/nod_1))) +'O'+str(int(abs(int(oxidation_states.get(elem_in_0[0])))/nod_1))).replace('1', '')
                product2 = (elem_in_0[1]+str(int((abs(int(oxidation_states.get('O')))/nod_2)))+'O'+ str(int(abs(int(oxidation_states.get(elem_in_0[1])))/nod_2))).replace('1', '')
                reaction = equation + '-->' + product1 + ' + ' + product2
                return balance_equation(reaction), 'горение'
        elif reagents[0] == 'CO' or reagents[1] == 'CO':
            reaction = reagents[0] + ' + ' + reagents[1] + ' --> ' + 'CO2'
            return balance_equation(reaction), 'горение'
        elif reagents[0]== 'SO2' or reagents[1] == 'SO2':
            reaction = reagents[0] + ' + ' + reagents[1] + ' --> ' + 'SO3'
            return balance_equation(reaction), 'горение'
        elif reagents[0] == 'P2O3' or reagents[1] == 'P2O5':
            reaction = reagents[0] + ' +' + reagents[1] + '-->' + 'P2O5'
            return balance_equation(reaction), 'горение'
        elif reagents[0] == 'Cu2O' or reagents[1] == 'Cu2O':
            reaction = reagents[0] + ' + ' + reagents[1] + '-->' + 'CuO'
            return balance_equation(reaction), 'горение'
        elif reagents[0] == 'NO' or reagents[1] == 'NO':
            reaction = reagents[0] + ' + ' + reagents[1] + '-->' + 'NO2'
            return balance_equation(reaction), 'горение'
        elif reagents[0] == 'CrO' or reagents[1] == 'CrO':
            reaction = reagents[0] + ' + ' + reagents[1] + '-->' + 'Cr2O3'
            return balance_equation(reaction), 'горение'
        elif reagents[0] == 'FeS' or reagents[1] == 'FeS':
            reaction = reagents[0] + ' + ' + reagents[1] + '-->' + 'Fe2O3' + ' + ' +  'SO2'
            return balance_equation(reaction), 'горение'
        elif reagents[0] == 'H2S' or reagents[1] == 'H2S':
            reaction = reagents[0] + ' + ' + reagents[1] + '-->' + 'SO2' + ' + ' + 'H2O'
            return balance_equation(reaction), 'горение'
        elif reagents[0] == 'NH3' or reagents[1] == 'NH3':
            reaction =  reagents[0] + ' + ' + reagents[1] + '-->' + 'NO' + ' + ' +  'H2O'
            return balance_equation(reaction), 'горение'
                                                                                                                                                                                                                                                             
def neutralization(equation, f = devision_into_parts): ##нейтрализация
    reagents = f(equation)
    if ('OH' in reagents[0] or 'OH' in reagents[1]) and ('H' in reagents[0] or 'H' in reagents[1]):
        if 'OH' in reagents[1]:
            base = reagents[1]
            reagents[1] = reagents[0]
            reagents[0] = base
        me = release_of_metal(reagents[0])
        a_ox = release_of_acid_residue(reagents[1])
        nod = gcd(abs(int(oxidation_states.get(me))),abs(int(acid_oxides_states.get(a_ox))))
        product = me + str(int(int(acid_oxides_states.get(a_ox))/nod)) + '(' + a_ox + ')' + str(int(int(oxidation_states.get(me))/nod))
        reaction =  equation + '-->' + product + ' + ' + 'H2O'
        if me+'1' in product and  ')1' in product:
            product1 = product.replace('1', '').replace(')', '').replace('(', '')
            return balance_equation(reaction.replace(product, product1)), 'обмен (нейтрализация)'
        if int(acid_oxides_states.get(a_ox))!=1 and ')1' in product:
            product2 = product.replace('(', '').replace(')1', '')
            return balance_equation(reaction.replace(product, product2)), 'обмен (нейтрализация)'
        if me+'1' in product:
            product3 = product.replace('1', '')
            return balance_equation(reaction.replace(product, product3)), 'обмен (нейтрализация)'
        else:
            return balance_equation(reaction), 'обмен (нейтрализация)'

def substitution(equation, f = devision_into_parts): ##замещение (металл +кислота, металл + соль, галоген + соль c галогеном)
    reagents = f(equation)
    if reagents[1] in Me or reagents[1] in Ne_Me:
        elem = reagents[1]
        reagents[1] = reagents[0]
        reagents[0] = elem
    ac_ox = release_of_acid_residue(reagents[1])
    elem0 = devision_into_elements(reagents[0])
    elem1 = devision_into_elements(reagents[1])
    if (reagents[0] in Me or reagents[1] in Me) and ('H' in reagents[0] or 'H' in reagents[1]):
        if (metal_activity_series.index(reagents[0])>metal_activity_series.index('H')):
            nod = gcd(abs(int(oxidation_states.get(reagents[0]))), abs(int(acid_oxides_states.get(ac_ox))))
            reaction = equation + '-->' + reagents[0]+str(int(int(acid_oxides_states.get(ac_ox))/nod)) + ac_ox  + str(int(int(oxidation_states.get(reagents[0]))/nod)).replace('1', '') + ' + ' + 'H2'
            if reagents[0]+str(int(int(acid_oxides_states.get(ac_ox))/nod))+'(' + ac_ox + ')' + str(int(int(oxidation_states.get(reagents[0]))/nod)) not in non_existent:
                return balance_equation(reaction), 'замещение'
            else:
                return 'Реакция не идет'
        else:
            return 'Реакция не идет'
    if (reagents[0] in Me or reagents[1] in Me) and (release_of_metal(reagents[1])):
        me_new = release_of_metal(reagents[1])
        if (metal_activity_series.index(reagents[0])>metal_activity_series.index(me_new)):
            nod = gcd(abs(int(oxidation_states.get(reagents[0]))), abs(int(acid_oxides_states.get(ac_ox))))
            reaction = equation + '-->' + (reagents[0]+str(int(int(acid_oxides_states.get(ac_ox))/nod)) + ac_ox  + str(int(int(oxidation_states.get(reagents[0]))/nod))).replace('1', '') + ' + ' +  me_new
            return balance_equation(reaction), 'замещение'
        else:
            return 'Реакция не идет'

    if (elem0[0] in halogene_strength) and (elem1[1] in halogene_strength):
        if halogene_strength.index(elem0[0]) > halogene_strength.index(elem1[1]):
            reaction = equation + '-->' + reagents[0].replace(elem0[0], elem1[1])+ ' + ' + reagents[1].replace(elem1[1], elem0[0])
            return balance_equation(reaction), 'замещение'
        else:
            return 'Реакция не идет'

def compound(equation, f = devision_into_parts): ##(соединение: 1+1, Ме + вода, кисотный/основный оксид + вода)
    reagents = f(equation)
    elem0 = devision_into_elements(reagents[0])
    elem1 = devision_into_elements(reagents[1])
    str_elem0 = ', '.join(elem0)
    str_elem1 = ', '.join(elem1)
    if (str_elem0 in Me) and (str_elem1 in Me) and (len(elem0) == 1 and len(elem1) ==1):
        return 'Реакция не идет'
    if 'H2' in equation and ('Si' in equation or 'B' in equation or 'P' in equation):
        return 'Реакция не идет'
    if (str_elem0 in Me or str_elem0 in Ne_Me) and (str_elem1 in Me or str_elem1 in Ne_Me) and (len(elem0) == 1 and len(elem1) ==1):
        nod = gcd(abs(int(oxidation_states.get(elem0[0]))), abs(int(oxidation_states.get(elem1[0]))))
        k1 = int(abs(int(oxidation_states.get(elem0[0]))))
        k2 = int(abs(int(oxidation_states.get(elem1[0]))))
        product = (elem0[0] + str(int(k2/nod)) + elem1[0] + str(int(k1/nod))).replace('1', '')
        reaction = equation + ' --> '  + product
        return balance_equation(reaction), 'соединение'
    if (reagents[1] == 'H2O' or reagents[0] == 'H2O'):
        if reagents[0] == 'H2O':
                water = reagents[1]
                reagents[1] = reagents[0]
                reagents[0] = water
        if (reagents[0] in ac_oxide or reagents[1] in ac_oxide):
            reaction =  equation + '-->' + acids_ox.get(reagents[0])
            return balance_equation(reaction), 'соединение'
        if (reagents[0] in b_oxide or reagents[1] in b_oxide):
            reaction =  equation + '-->' + base_ox.get(reagents[0])
            return balance_equation(reaction), 'соединение'
        if reagents[0] in Me:
            me = release_of_metal(reagents[0])
            product = reagents[0]+ '(OH)' + str(int(oxidation_states.get(reagents[0])))
            reaction = equation + '-->' + product + ' + ' +'H2'
            if ')1' in product:
                product1 = product.replace('(', '').replace(')1', '')
            if product not in sediment or product1 not in sediment:
                return balance_equation(reaction.replace(product, product1)), 'соединение'
            else:
                return 'Реакция не идет'

def exchange(equation, f = devision_into_parts): ##обмен: соль + соль
    reagents = f(equation)
    if reagents[0] not in sediment and reagents[1] not in sediment:
        elem0 = devision_into_elements(reagents[0])
        elem1 = devision_into_elements(reagents[1])
        a_ox0 = release_of_acid_residue(reagents[0])
        a_ox1 = release_of_acid_residue(reagents[1])
        me0 = release_of_metal(reagents[0])
        me1 = release_of_metal(reagents[1])
        nod0 = gcd(abs(int(oxidation_states.get(elem0[0]))),abs(int(acid_oxides_states.get(a_ox1))))
        nod1 = gcd(abs(int(oxidation_states.get(elem1[0]))),abs(int(acid_oxides_states.get(a_ox0))))
        product1 = elem0[0] + str(int(int(acid_oxides_states.get(a_ox1))/nod0)) + '(' + a_ox1 + ')' + str(int(int(oxidation_states.get(elem0[0]))/nod0))
        product2 = elem1[0] + str(int(int(acid_oxides_states.get(a_ox0))/nod1)) +'(' +  a_ox0 + ')' + str(int(int(oxidation_states.get(elem1[0]))/nod1))
        if (me0+'1(' in product1) and  (')1' in product1):
            product1 = product1.replace('1(', '').replace(')1', '')
        elif me0+'1' in product1:
            product1 = product1.replace('1', '')
        elif int(acid_oxides_states.get(a_ox1))!=1 and ')1' in product1:
            product1 = product1.replace('(', '').replace(')1', '')
        if me1+'1' in product2:
            product2 = product2.replace('1', '')
        elif me1+'1(' in product2 and  ')1' in product2:
            product2 = product2.replace('1(', '').replace(')1', '')
        elif int(acid_oxides_states.get(a_ox0))!=1 and ')1' in product2:
            product2 = product2.replace('(', '').replace(')1', '')
        if (product1 in sediment) or (product2 in sediment):
            reaction = equation + '-->' + product1 + ' + ' + product2
            return balance_equation(reaction), 'обмен'
        else:
            return 'Реакция не идет'
            
            
            
