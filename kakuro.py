kakuro = [
["B","B","B","B","B",(29,"B"),(17,"B"),"B","B"],
["B","B","B","B",("B",16),"W","W",(30,"B"),(23,"B")],
["B","B","B","B",(22,29),"W","W","W","W"],
["B","B",(30,"B"),(3,3),"W","W",(7,17),"W","W"],
["B",(24,33),"W","W","W","W","W","W","W"],
[("B",41),"W","W","W","W","W","W","W","B"],
[("B",16),"W","W",(11,14),"W","W","B","B","B"],
[("B",28),"W","W","W","W","B","B","B","B"],
["B","B",("B",9),"W","W","B","B","B","B"]]

def print_kakuro(kakuro):
    for rows in kakuro[0]:
        print(rows)
    return

def tuples_sorting(value_cols_down):    #SUB FUNCTION count_col_down__spaces
    if type(value_cols_down) != type(("#","#")):
        return str(value_cols_down)
    else:
        return value_cols_down

def space_counter(spaces_count, type_tuple):    #SUB FUNCTION count_col_down__spaces

    if type_tuple == 2 or type_tuple == 1: #(#,#) WHITES DOWN
        coordinate_tuple = 0
        spaces_tuple_till_next = 0
        found_tuple = False
        for spaces in spaces_count:

            if type(spaces) != type(("#","#")) and found_tuple == False:
                coordinate_tuple += 1
                spaces_tuple_till_next += 1
                continue
            elif found_tuple == False:
                found_tuple = True
            elif found_tuple == True and spaces == 'W':
                spaces_tuple_till_next += 1
            else:
                break
            
        return[coordinate_tuple, spaces_tuple_till_next]

        


def count_col_down__spaces(kakuro,fils,cols):
    pos_tuple = kakuro[fils][cols]
    
    cols_down = [filas[cols+1] for filas in kakuro]
    str_array = [tuples_sorting(values_cols_down) for values_cols_down in cols_down]
    whites_till_next = space_counter(str_array, type_tuple=1)
    print(str_array)
    print(str_array[whites_till_next[0]], str_array[whites_till_next[1]+1])
    print(whites_till_next)
    return [whites_till_next]
    #RETURN A BREAK

def count_fil_left_spaces(kakuro,fils,cols):
    print()

def classify_tuples(c_tuple):
    if c_tuple[0] != "B" and type(c_tuple[1]) == type(0): 
        return 0
    elif type(c_tuple[0]) == type(0) and c_tuple[1] != "B": 
        return 1
    else: #Both Numbers
        return 2 

def execute_setting(kakuro,fils,cols,psble_values, setting_values, coordinates_trayectory):
    numers_list_horizontal=[]
    # Revisar la fila (horizontal)
    kakuro_column = [fila[cols] for fila in kakuro][coordinates_trayectory[0][0]+1:coordinates_trayectory[0][1]]
    for numbers in kakuro_column:
        if type(numbers) == type(0):
            numers_list_horizontal.append(numbers)

    if psble_values in numers_list_horizontal: #turn into numbers #turn into numbers
        return False

    elif kakuro[fils][cols][0] < sum(numers_list_horizontal) and setting_values < coordinates_trayectory[0][1] - coordinates_trayectory[0][0]:
        return False

    elif kakuro[fils][cols][0] == sum(numers_list_horizontal) and setting_values == coordinates_trayectory[0][1] - coordinates_trayectory[0][0]:
        return False
	# revisar la columna (vertical)
    column = [fila[cols] for fila in kakuro] #turn into numbers without tuples
    if psble_values in column:
        return False
    
    return True

def print_kankuro(kakuro):
    for fils in range(len(kakuro)):
        for cols in range(len([filas[0] for filas in kakuro])):
            if type(kakuro[fils][cols]) == type(("#","#")):
                tipo = classify_tuples(kakuro[fils][cols])
                if tipo == 0:#(#, B) down
                    coordinates_trayectory = count_col_down__spaces(kakuro,fils,cols)
                    #CHECK THIS COORDINATES LATER
                    for setting_values in range(coordinates_trayectory[0][1] - coordinates_trayectory[0][0]): #times to run setter after tuple
                        print(kakuro[setting_values+1][cols])
                        for psble_values in range(15):
                            if execute_setting(kakuro,fils,cols,psble_values, setting_values+1, coordinates_trayectory):
                                
                                print(kakuro[setting_values+1][cols])
                                kakuro[setting_values+1][cols] = psble_values
                                # print(kakuro)
                                print_kankuro(kakuro)
                                kakuro[fils][cols] = 0
                        else:
                            return
                elif tipo == 1:#(B,#) left
                    coordinates_trayectory = count_fil_left_spaces(kakuro,fils,cols)
                elif tipo == 2:#(#,#) down/left
                    coordinates_trayectory = count_col_down__spaces(kakuro,fils,cols)

    print_kakuro(kakuro)
                        

print_kankuro(kakuro)