def format_line(line):
    r = {}
    line = line.split(',')
    r["nom"] = line[0].split('=')[0].strip()
    r["position"] = line[0].split('=')[1].split(':')[1].strip()
    r["number"] = line[1].split('=')[0].split(':')[1].strip()
    r["small"] = line[2].split('=')[0].split(':')[1].strip()
    r["molar"] = line[3].split('=')[0].split(':')[1].strip()
    r["electron"] = line[4].split('=')[0].split(':')[1].strip()
    return r


def my_html():
    page = """<!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <title>Periodic Table</title>
                    <link rel="stylesheet" href="style.css">
                </head>
            <body>
                <h1>Hello Periodic Table</h1>
                <table>
            """
    elements = []
    with open('periodic_table.txt', 'r') as f:
        for line in f:
            e = format_line(line)
            elements.append(e)
    page += "<tr>"
    position = -1
    for e in elements:
        if position + 1 != int(e["position"]):
            n = abs(position + 1 - int(e["position"]))
            print(n)
            for i in range(0, n):
                page += "<td></td>"
        position = int(e["position"])
        page += f"""<td style='border: 1px solid black; padding:10px'>
                    <h2> {e["nom"]} </h2>
                    <ul><li> {e["number"]} </li>
                    <li> {e["small"]} </li>
                    <li> {e["molar"]} </li>
                    <li> {e["electron"]} </li>
                    </ul>
                    </td>"""
        if position == 17:
            position = -1
            page += "</tr>"
            page += "<tr>"
    page = page[:-4]
    page += "</table>"
    page += "</body>"
    page += "</html>"
    with open('periodic_table.html', 'w') as f:
        f.write(page)

if __name__ == '__main__':
    my_html()