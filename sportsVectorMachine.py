import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

def find_strike_zone(data): 
  fig, ax = plt.subplots()
  #print(aaron_judge.columns)
  #print(aaron_judge.description.unique())
  print(data.type.unique())
  data.type = data.type.map({'S':1, 'B':0})
  print(data.type)
  data = data.dropna(subset = ["plate_x", "plate_z", "type"])
  plt.scatter(x = data.plate_x, y = data.plate_z, c = data.type, cmap = plt.cm.coolwarm, alpha = 0.5 )

  training_set, validation_set = train_test_split(data, random_state = 1)
  l = {'score':0, 'gamma':1, 'C':1}
  for C in range(1,10):
    for gamma in range(1, 10):
      classifier = SVC(gamma = gamma, C = C)
      classifier.fit(training_set[['plate_x', 'plate_z']], training_set.type)
      score = classifier.score(validation_set[['plate_x', 'plate_z']], validation_set.type)
    if score > l['score']:
      l['score'] = score
      l['gamma'] = gamma
      l['C'] = C

  print(l)
  draw_boundary(ax, classifier)
  ax.set_ylim(-2, 6)
  ax.set_xlim(-3, 3)
  plt.show()
#find_strike_zone(aaron_judge)
find_strike_zone(jose_altuve)
