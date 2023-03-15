import xlrd

def read_file(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    rows = table.nrows
    data = []
    for v in range(1, rows):
        values = table.row_values(v)
        data.append(
            (
                {
                    "department": str(values[0]),
                    "name": str(values[1]),
                    "ID": str(values[2]),
                    "password": str(values[3]),
                    "gender": str(values[4]),
                    "age": str(values[5]),
                    "performance": str(values[6])
                }
            )
        )
    return data


if __name__ == '__main__':
    d1 = read_file('./init.xls')
    d2 = str(d1).replace("\'", "\"")
    jsFile = open('./init.json', 'w+', encoding='utf-8')
    jsFile.write(d2)
    jsFile.close()