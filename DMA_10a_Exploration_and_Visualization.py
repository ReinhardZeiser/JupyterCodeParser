# Modul matplotlib.pyplot importieren und Anzeige der Grafiken im Notebook aktivieren
import matplotlib.pyplot as plt
#from __future__ import division# Beispiel 1: einfaches Liniendiagramm (line chart)

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp)
plt.show()# Liniendiagramm formatieren: z.B. Farbe, Marker, Linienart, Titel und Labels

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# add a title
plt.title("Nominal GDP")

# add a label to the y-axis
plt.ylabel("Billions of $")
plt.xlabel("year")
plt.show()# Übersicht über die Funktion plot im Modul matplotlib.pyplot
# "args" = arguments (variable Länge, z.B. years, gdp)
# "kwargs" = keywordes arguments (z.B. color='green')
# fmt = shortcut string notation for defining basic formatting like color, marker and linestyle

# Beispiel 2a: einfaches Säulendiagramm

plt.bar(range(10), range(10))    # plt.bar(Position für Beginn des Balkens auf x-Achse, Höhe des Balkens auf y-Achse)
plt.show()# Beispiel 2a: einfaches Säulendiagramm

plt.bar(range(10), range(10), 0.5)    # plt.bar(x-Achse, y-Achse, Balkenbreite)
plt.show()# Beispiel 2b: Säulendiagramm "Oscars" (bar chart)

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# plot bars with left x-coordinates [xs], heights [num_oscars]
xs = [i for i, _ in enumerate(movies)]
plt.bar(xs, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

# label x-axis with movie names at bar centers
plt.xticks([i for i, _ in enumerate(movies)], movies)

plt.show()# Funktion Counter: Mapping von keys zu counts (Anzahl des Vorkommens) - hilfreich zur Erstellung von Histogrammen
from collections import Counter            
c = Counter([0, 1, 2, 0])
print(c)# Beispiel 3: Histogramm klassifizierter Daten als Säulendiagramm abbilden

grades = [83,95,91,87,70,0,85,82,100,
          67,73,77,0]
decile = lambda grade: grade // 10 * 10    # Abbildung der Werte auf Dezile - so wird z.B. 83 zu 80, 95 zu 90 etc.

histogram = Counter(decile(grade) for grade in grades)

plt.bar([x for x in histogram.keys()],     # key: hier = Dezile
        histogram.values(),                # value: hier = Anzahl Fälle je Dezil (gezählt durch Counter)
        8)                                 # give each bar a width of 8 - so bleiben Lücken, da Balkenbreite = 10

plt.axis([-5, 105, 0, 5])                  # x-axis from -5 to 105, y-axis from 0 to 5
plt.xticks([10 * i for i in range(11)])    # x-axis labels at 0, 10, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()# Achtung bei der Formatierung der Achsen!
# Beispiel 4a: Irreführende Darstellung durch unangemessene Achsenformatierung

mentions = [500, 505]
years = [2013, 2014]

# plt.bar([2012.6, 2013.6], mentions, 0.8)

plt.bar(years, mentions, 0.8)

plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")

# misleading y-axis only shows the part above 500
plt.axis([2012.5,2014.5,499,506])
plt.title("Look at the 'Huge' Increase!")
plt.show()# Beispiel 4b: Angemessenere Darstellung

mentions = [500, 505]
years = [2013, 2014]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")


# force y-axis to start at 0
plt.axis([2012.5,2014.5,0,550])      # dies entspricht der default-Einstellung, könnte also weggelassen werden
plt.title("Not So Huge Anymore.")
plt.show()# Beispiel 5: Abbildung mehrerer Linien in einem Diagramm

variance     = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
total_error  = [x + y for x, y in zip(variance, bias_squared)]

xs = range(len(variance))

# we can make multiple calls to plt.plot 
# to show multiple series on the same chart
plt.plot(xs, variance,     'g-',  label='variance')    # green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2')      # red dot-dashed line
plt.plot(xs, total_error,  'b:',  label='total error') # blue dotted line

# because we've assigned labels to each series
# we can get a legend for free
# loc=9 means "top center"
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()# Beispiel 6: Scatterplots
# Anzahl Freunde vs Anzahl verbrachter Minuten pro Tag im Sozialen Netzwerk

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)
    
# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count), # put the label with its point
                 xytext=(5, -5),                  # but slightly offset
                 textcoords='offset points')

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()# Beispiel 7a: Achsenformatierung bei Scatterplots - per Default wird die Skala für jedes Merkmal individuell festgelegt
# Das kann bei vergleichbaren Merkmalen zu Fehlinterpretationen führen

test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")

plt.title("Axes Aren't Comparable")

plt.show()# Beispiel 7b: Aufruf plt.axis("equal"): gleiche Skala für beide Achsen
# So sieht man, dass die Ergebnisse von test 2 eine deutlich stärkere Streuung aufweisen

plt.scatter(test_1_grades, test_2_grades)
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")

plt.axis("equal")
plt.title("Axes Are Comparable")

plt.show()# Beispiel 8: einfaches Kreisdiagramm

plt.pie([0.95, 0.05], labels=["Uses pie charts", "Knows better"])

# make sure pie is a circle and not an oval
plt.axis("equal")
plt.show()# Import erforderlicher Funktionen / Module
import matplotlib.pyplot as plt
#from __future__ import division
#from collections import Counter
import math# Betrachtung der Verteilung von einem einzelnem Merkmal, z.B. Anzahl Freunde in einem Sozialen Netzwerk - Daten:

num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,
               10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,
               6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,
               4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,
               1,1,1,1,1,1,1,1,1,1]# Abbildung der Verteilung als absolute Häufigkeiten in einem Histogramm

friend_counts = Counter(num_friends)    # Zu jedem Wert (key) wird die Häufigkeit des Auftretens gemappt (value)
xs = range(101)
ys = [friend_counts[x] for x in xs]     # Aufruf des Values (abs Häufigkeit) je key (für Werte von 0 bis 100)

plt.bar(xs, ys)                         # Plotten von Balken an Position xs (0 bis 100) mit Höhe ys (Häufigkeit)
plt.axis([0,101,0,25])                  # Festlegen der Skala von x- und y-Achse
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()# Ausschnitt des Histogramms (ohne Extremwerte)

friend_counts = Counter(num_friends)    # Zu jedem Wert (key) wird die Häufigkeit des Auftretens gemappt (value)
xs = range(101)
ys = [friend_counts[x] for x in xs]     # Aufruf des Values (abs Häufigkeit) je key (für Werte von 0 bis 100)

plt.bar(xs, ys)                         # Plotten von Balken an Position xs (0 bis 100) mit Höhe ys (Häufigkeit)
plt.axis([0,30,0,25])                  # Festlegen der Skala von x- und y-Achse
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()# Berechnung statistischer Kennwerte: Anzahl Werte, Min, Max

num_points = len(num_friends)
largest_value = max(num_friends)
smalles_value = min(num_friends)
print("Anzahl Werte =", num_points, ", Maximum =", largest_value, ", Minimum =", smalles_value)# Mittelwert (Achtung: funktioniert nur mit Division 'from future')

def mean(x):
    return sum(x) / len(x)
mean(num_friends)# Median: komplizierter wegen Unterscheidung gerade/ungerade Anzahl Werte

def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = (n // 2)                                 
    
    if n % 2 == 1:
        # if odd, return the middle value                  ++ Bsp: 13 Fälle --> mittlerer Wert ist der 7. Wert (Index=6)
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values ++ Bsp: 12 Fälle --> Mittelwert von 6.+7. Wert (Index = 5 und 6)
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

print(median([1, 2, 3]))
print(median([1, 2, 3, 4]))
print(median(num_friends))# Quantile

def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

print(quantile(num_friends, 0.10), quantile(num_friends, 0.25), quantile(num_friends, 0.75), quantile(num_friends, 0.90))# Modus

def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]



mode(num_friends)# Absolute Häufigkeiten der häufigsten Werte zählen
print(friend_counts[1], friend_counts[6])# Spannweite

# "range" already means something in Python, so we'll use a different name
def data_range(x):
    return max(x) - min(x)

data_range(num_friends)# Varianz und Standardabweichung

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """mittlere quadrierte Abweichung vom Mittelwert (assumes x has at least two elements)"""
    n = len(x)
    deviations = de_mean(x)
    return sum([i**2 for i in deviations]) / n
    
def standard_deviation(x):
    """Wurzel aus der Varianz"""
    return math.sqrt(variance(x))

print(variance(num_friends), standard_deviation(num_friends))# Interquartilsabstand

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

interquartile_range(num_friends)# Boxplot

plt.boxplot(num_friends)
plt.show()# Betrachtung der gemeinsamen Verteilung von zwei Merkmalen, z.B. Anzahl Freunde und Minuten Online - Daten des 2. Merkmals:

daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,
                 36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,
                 27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,
                 26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,
                 24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,
                 25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,
                 14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,
                 13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,
                 28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,
                 25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,
                 20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,
                 24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]# Correlation
# Berechnung gemäß Definition als gemeinsame Streuung von zwei Merkmalen (Kovarianz),
# geteilt durch Produkt der beiden einzelnen Streuungen (Standardabweichung)
# Korrelation liegt immer zwischen -1 und 1 (negative/positive Korrelation), wenn nahe an 0 = geringe Korrelation

def dot(v,w):                                   # Funktion zur Bildung der Summe aus paarweisen Produkten 2er Listen
    return sum(v_i * w_i
               for v_i, w_i in zip(v,w))

def covariance(x, y):                           # Kovarianz als Mittelwert der Summe der paarweisen Produkte der
    n = len(x)                                  # jeweiligen Abweichungen der beiden Merkmalsausprägungen vom Mittelwert  
    return dot(de_mean(x), de_mean(y)) / n

def correlation(x, y):                          # Korrelation = Kovarianz / Stddev_x * Stddev_y
    stdev_x = standard_deviation(x)              
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero

correlation(num_friends, daily_minutes)# Betrachtung im Scatterplot - Ausreißer?

plt.scatter(num_friends, daily_minutes)

plt.axis([0, 105, 0, 100])    
plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()# Korrelation ohne Berücksichtigung des Ausreißers (= 100 Freunde und 1 Minute)

outlier = num_friends.index(100) # index of outlier

num_friends_good = [x 
                    for i, x in enumerate(num_friends) 
                    if i != outlier]

daily_minutes_good = [x 
                      for i, x in enumerate(daily_minutes) 
                      if i != outlier]

correlation(num_friends_good, daily_minutes_good)