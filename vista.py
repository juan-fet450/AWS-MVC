#!/usr/bin/python3

import cgi, cgitb; cgitb.enable()
from string import Template
import xml.etree.cElementTree as ET

def views(mssge, usuar):
        print("Content-type: text/html; charset=utf-8\n\n")
        print(" ")
        table_headers = ET.Element('tr')
        th1 = ET.SubElement(table_headers, 'th', scope = 'col')
        th1.text = "Nombre"
        th2 = ET.SubElement(table_headers, 'th', scope = 'col')
        th2.text = "Valor"

        table_body = ET.Element('tbody')
        tr1 = ET.SubElement(table_body, 'tr')
        th1 = ET.SubElement(tr1, 'th', scope = 'row')
        th1.text = "Username"
        tr1_2 = ET.SubElement(tr1, 'td')
        tr1_2.text = "juan"

        tr2 = ET.SubElement(table_body, 'tr')
        th2 = ET.SubElement(tr2, 'th', scope = 'row')
        th2.text = "password"
        tr1_2 = ET.SubElement(tr2, 'td')
        tr1_2.text = "450"

        ths = ET.tostring(table_headers, "utf-8")
        tbody = ET.tostring(table_body, "utf-8")

        with open("vistahtml.html") as template:
                html_template = template.read()

        subst_dict = dict (
                title = "Bienvenido",
                header = usuar,
                message = mssge,
                ths=ths.decode("utf-8"),
                tbody=tbody.decode("utf-8"),
                footer="buenas noches"
        )
        print(Template(html_template).safe_substitute(subst_dict))

