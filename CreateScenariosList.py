from os import listdir
from os.path import isfile, join, dirname, abspath
import xml.etree.cElementTree as ET
import xml.dom.minidom as XDM

# CHANGE THIS PARAMETER TO CHANGE AUTOSTART TIMEOUT
autoStartDelay = "15" #seconds

scenariosList = "ScenariosList"
xmlExtension = ".xml"
ipPath = "https://raw.githubusercontent.com/scrabble-testcases/ui-automation/master/"


mypath = dirname(abspath(__file__))
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) and xmlExtension in f and not scenariosList in f]
onlyfiles.sort()

root = ET.Element("ScenarioList")
root.set("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
root.set("xmlns:xsd","http://www.w3.org/2001/XMLSchema")
root.set("AutoStartDelay",autoStartDelay)
scenarios = ET.SubElement(root, "Scenarios")

for f in onlyfiles:
   ET.SubElement(scenarios, "Scenario", Path = ipPath + f)
   
xml = XDM.parseString(ET.tostring(root,encoding = "utf-8", method = "xml"))
res = '\n'.join([line for line in xml.toprettyxml(indent='	', encoding = "utf-8").split('\n') if line.strip()])
scenariosListFullName = join(mypath,scenariosList + xmlExtension)
if isfile(scenariosListFullName) :
   f = open(scenariosListFullName,'r')
   existing = f.read()
   f.close()
else:
   existing = ""
if existing != res :
   f = open(scenariosListFullName,'w')
   f.write(res)
   f.close()
   print("\n File " + scenariosListFullName + " was changed.\n")
else :
   print("\n File " + scenariosListFullName + " was not changed.\n")
