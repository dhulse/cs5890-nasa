#!/usr/bin/python

import sys
import pandas as pd
from sklearn import tree
from sklearn.externals.six import StringIO
import sklearn
import pydot

FEATURES = ['nominal-AU-distance', 'v-relative', 'H']

# TARGET_TITLES = ['AMO*', 'APO*', 'ATE*', 'IEO*']

def get_df(file_path):
	return pd.read_csv(file_path)

def df_discretization(df):
	df['nominal-AU-distance'] = df['nominal-AU-distance'].apply(distance_discretization)
	df['v-relative'] = df['v-relative'].apply(velocity_discretization)
	df['H'] = df['H'].apply(size_discretization)
	df['class'] = df['class'].apply(type_discretization)
	return df

def distance_discretization(distance):
	if distance <= 0.1:
		return 0
	elif distance > 0.1 and distance <= 0.2:
		return 1
	elif distance > 0.2 and distance <= 0.3:
		return 2
	elif distance > 0.3 and distance <= 0.4:
		return 3
	elif distance > 0.4 and distance <= 0.5:
		return 5
	else:
		return 6

def velocity_discretization(vel):
	if vel <= 5:
		return 0
	elif vel > 5 and vel <= 10:
		return 1
	elif vel > 10 and vel <= 15:
		return 2
	elif vel > 15 and vel <= 20:
		return 3
	elif vel > 20 and vel <= 25:
		return 4
	elif vel > 25 and vel <= 30:
		return 5
	else:
		return 6

def size_discretization(size):
	if size <= 5:
		return 0
	elif size > 5 and size <= 10:
		return 1
	elif size > 10 and size <= 15:
		return 2
	elif size > 15 and size <= 20:
		return 3
	elif size > 20 and size <= 25:
		return 4
	elif size > 25 and size <= 30:
		return 5
	else:
		return 6

def type_discretization(t):
	if t == 'AMO*':
		return 0
	elif t == 'APO*':
		return 1
	elif t == 'ATE*':
		return 2
	elif t == 'IEO*':
		return 3
	elif t == 'ETc*':
		return 4
	elif t == 'HTC*':
		return 5
	elif t == 'JFc*':
		return 6
	else:
		return 7

def build_tree(df):
	learning_data = []
	learning_target_data = []
	print 'Creating Training Data Set...'
	for key, row in df.sample(frac=0.8).iterrows():
		learning_target_data.append(row['class'])
		learning_data.append([
			row['nominal-AU-distance'],
			row['v-relative'],
			row['H']
		])

	print 'Creating Testing Data Set...'
	testing_data = []
	for key, row in df.sample(frac=0.2).iterrows():
		testing_data.append({
			'target': row['class'],
			'input': [
				row['nominal-AU-distance'],
				row['v-relative'],
				row['H']
			]
		})

	print 'Building Tree Classifier...'
	clf = tree.DecisionTreeClassifier(min_samples_split=1000)
	clf = clf.fit(learning_data, learning_target_data)

	print 'Testing Tree Classifier'
	correct_results = 0
	for row in testing_data:
		if clf.predict([row['input']])[0] == row['target']:
			correct_results += 1

	print 'Matched correctly: {0}'.format(correct_results)
	print 'Mismatched: {0}'.format(len(testing_data) - correct_results)
	print 'Number of tests: {0}'.format(len(testing_data))

	print 'Exporting to JSON'
	print treeToJson(clf)
	# print 'Creating Visual for Tree Classifier'
	# dot_data = StringIO()
	# tree.export_graphviz(clf, feature_names=FEATURES, out_file=dot_data)
	# graph = pydot.graph_from_dot_data(dot_data.getvalue())
	# graph.write_png('ufos.png')



# Code treeToJson from: https://www.garysieling.com/blog/convert-scikit-learn-decision-trees-json
def treeToJson(decision_tree, feature_names=None):
  from warnings import warn
 
  js = ""
 
  def node_to_str(tree, node_id, criterion):
    if not isinstance(criterion, sklearn.tree.tree.six.string_types):
      criterion = "impurity"
 
    value = tree.value[node_id]
    if tree.n_outputs == 1:
      value = value[0, :]
 
    jsonValue = ', '.join([str(x) for x in value])
 
    if tree.children_left[node_id] == sklearn.tree._tree.TREE_LEAF:
      return '"id": "%s", "criterion": "%s", "impurity": "%s", "samples": "%s", "value": [%s]' \
             % (node_id, 
                criterion,
                tree.impurity[node_id],
                tree.n_node_samples[node_id],
                jsonValue)
    else:
      if feature_names is not None:
        feature = feature_names[tree.feature[node_id]]
      else:
        feature = tree.feature[node_id]
 
      if isinstance(feature, basestring) and "=" in feature:
        ruleType = "="
        ruleValue = "false"
      else:
        ruleType = "<="
        ruleValue = "%.4f" % tree.threshold[node_id]
 
      return '"id": "%s", "rule": "%s %s %s", "%s": "%s", "samples": "%s"' \
             % (node_id, 
                feature,
                ruleType,
                ruleValue,
                criterion,
                tree.impurity[node_id],
                tree.n_node_samples[node_id])
 
  def recurse(tree, node_id, criterion, parent=None, depth=0):
    tabs = "  " * depth
    js = ""
 
    left_child = tree.children_left[node_id]
    right_child = tree.children_right[node_id]
 
    js = js + "\n" + \
         tabs + "{\n" + \
         tabs + "  " + node_to_str(tree, node_id, criterion)
 
    if left_child != sklearn.tree._tree.TREE_LEAF:
      js = js + ",\n" + \
           tabs + '  "left": ' + \
           recurse(tree, \
                   left_child, \
                   criterion=criterion, \
                   parent=node_id, \
                   depth=depth + 1) + ",\n" + \
           tabs + '  "right": ' + \
           recurse(tree, \
                   right_child, \
                   criterion=criterion, \
                   parent=node_id,
                   depth=depth + 1)
 
    js = js + tabs + "\n" + \
         tabs + "}"
 
    return js
 
  if isinstance(decision_tree, sklearn.tree.tree.Tree):
    js = js + recurse(decision_tree, 0, criterion="impurity")
  else:
    js = js + recurse(decision_tree.tree_, 0, criterion=decision_tree.criterion)
 
  return js



def main(file_path):
	print 'Reading Dataframe...'
	df = get_df(file_path)
	print 'Doing Discretization...'
	df = df_discretization(df)
	print 'Build Tree Classifier...'
	build_tree(df)

if __name__ == '__main__':
	main(sys.argv[1])