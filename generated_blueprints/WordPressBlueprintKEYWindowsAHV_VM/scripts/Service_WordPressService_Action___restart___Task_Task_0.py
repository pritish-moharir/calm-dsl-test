# python3;success
xml_val = """<breakfast_menu>
<food>
<name>Belgian Waffles</name>
<price>$5.95</price>
<description>Two of our famous Belgian Waffles with plenty of real maple syrup</description>
<calories>650</calories>
</food>
</breakfast_menu>
"""
xml_root = xml.etree.ElementTree.fromstring(xml_val)
for i in range(1):
    print(
        "cost of",
        xml_root[i][0].text,
        "is",
        xml_root[i][1].text,
        "with",
        xml_root[i][3].text,
        "calories",
    )
# python3;success
xml_val = """<breakfast_menu>
<food>
<name>Belgian Waffles</name>
<price>$5.95</price>
<description>Two of our famous Belgian Waffles with plenty of real maple syrup</description>
<calories>650</calories>
</food>
</breakfast_menu>
"""
xml_root = xml.etree.ElementTree.fromstring(xml_val)
for i in range(1):
    print(
        "cost of",
        xml_root[i][0].text,
        "is",
        xml_root[i][1].text,
        "with",
        xml_root[i][3].text,
        "calories",
    )
