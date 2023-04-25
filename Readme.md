# Graphic Ptolemaic Bound

Dieses kleine Projekt dient dazu, sich die ptolomäische Ungleichung grafisch veranschaulichen zu
lassen. Genauer gesagt die untere Schranke, die sich aus der ptolomäischen Ungleichung ergibt.
Dazu stehen in der Datei "visualizations" drei verschiedene Methoden zur Verfügung.

### Die Gestaltung der Plots
Die Plots stellen jeweils einen Ausschnitt aus dem zweidimensionalen Raum dar. Die Fläche wird
dabei in verschiedene Gebiete eingeteilt und gefärbt, je nachdem welchen Wert die durch die
ptolomäische Ungleichung ermittelte untere Distanzabschätzung für Punkte in diesem Bereich annimmt.
Punkte, die aus Sicht der ptolomäischen Schranke nah am Queryobjekt liegen, werden in verschieden
starken Rottönen markiert. Dies gilt für Werte im Bereich 0 bis 4, wobei die Abstufungen werden in
1er-Schritten vorgenommen. Punkte, bei denen die ptolomäische Schranke Werte zwischen 4 und 10 ergibt,
sind beige gefärbt. Punkte im Bereich 10 bis 20 werden blau eingefärbt, während Punkte mit noch höheren
Werten weiß bleiben. Diese Aufteilung hat sich nach einigem Herumprobieren ergeben und für mich als
äußerst praktisch herausgestellt. Sie visualisiert, welche Punkte aus der ptolomäischen Sicht sehr nah
am Pivotelement sind und daher nicht gefiltert werden, und wie sich die Schranke in diesem Bereich
ausbreitet. Gleichzeitig erhält man anhand des Plots ein gutes Gefühl dafür, welche Punkte eine
besonders hohe untere Schranke erhalten und damit besonders gut ausgeschlossen werden können. Die
groben Zwischenschritte erlauben es, den Verlauf zu erahnen, während die Übersichtlichkeit gewahrt
wird. Diese Aufteilung ist natürlich Geschmackssache und kann angepasst werden. Für mich hat sie, wie
gesagt, gute Dienste geleistet.

### Die drei Plots
Die erste Methode, "ptolemy_bound_vector_space", stellt dabei die grundlegende Funktionalität dar, indem sie
einen Plot für die ptolomäische Schranke bei einem Querypunkt und zwei Pivotelementen erstellt. 

Darauf aufbauend gibt es die Methode "ptolemy_bound_vector_space_triple". Diese betrifft die Situation
mit drei Pivotelementen. Bei drei Pivotelementen gibt es drei Paare von Pivotelementen, sodass mit Hilfe der
ptolomäischen Ungleichung drei untere Schranken aufgestellt werden können. Es wird ein Plot erstellt, der 
das Maximum dieser drei Schranken (welches damit selbst eine untere Schranke darstellt) abbildet. Mit
dieser Methode kann das Zusammenspiel mehrerer Schranken untersucht werden. Insbesondere stellt sich die Frage,
welche Lage der Pivotelemente zueinander (und zum Queryobjekt) besonders günstig ist, d.h. besonders viele
Punkte ausschließen kann (d.h. besonders kleiner roter Bereich).

Zuletzt gibt es eine Methode "ptolemy_bound_pivot_space", mit der die ptolomäische Schranke im Pivotraum,
dargestellt wird. In diesem Fall ergibt sich eine Art Strahl oder Band. Dies lässt sich durch eine Rechnung
auch leicht mathematisch verifizieren.


