import pdb
import pandas as pd
import numpy as np



def generate_statistic(predicted_y,actual_y,clf=None,all_possible_outputs=None,cm_include_indecisive=False):
    if all_possible_outputs is None and clf is None:
        all_possible_outputs = list(set(predicted_y.unique().tolist() + actual_y.unique().tolist()))
    if clf is not None:
        all_possible_outputs = clf.classes_

    all_possible_outputs.sort()

    zero_or_na = [0,None]
    all_output_labels = all_possible_outputs
    df = pd.DataFrame({'actual_y':actual_y.tolist(),'predicted_y':predicted_y.tolist()})

    N = 0 ####total number of transactions excluding indecisive
    for output_label in all_output_labels:
        N += len(df[df['predicted_y'] == output_label])

    result = {'||total(excluding_indecisive)': N,'||indecisive_total': len(df) - N}
    result.update({'||indecisive_proportion':result['||indecisive_total']/len(df)})
    total_number_of_correctly_classified = 0
    for output_label in all_output_labels:
        rule_antecedent_count = len(df[df['predicted_y'] == output_label])
        number_of_correctly_classified = len(df[(df['predicted_y'] == output_label) & (df['actual_y'] == output_label)])
        number_of_correct_label = len(df[(df['actual_y'] == output_label)])
        support_of_correct_label = number_of_correct_label/N if N not in zero_or_na else 0
        number_of_incorrectly_classified = len(df[(df['predicted_y'] == output_label) & (df['actual_y'] != output_label)])
        support = number_of_correctly_classified/N if N not in zero_or_na else None
        confidence = number_of_correctly_classified/rule_antecedent_count if rule_antecedent_count not in zero_or_na else None
        lift = confidence/support_of_correct_label if support_of_correct_label not in zero_or_na and confidence not in zero_or_na else None
        result['output_label={}|correctly_classified_count'.format(output_label)] = number_of_correctly_classified
        result['output_label={}|incorrectly_classified_count'.format(output_label)] = number_of_incorrectly_classified
        result['output_label={}|support'.format(output_label)] = support
        result['output_label={}|confidence'.format(output_label)] = confidence
        result['output_label={}|lift'.format(output_label)] = lift
        result['output_label={}|cases_satisfying_antecedent_count'.format(output_label)] = rule_antecedent_count
        total_number_of_correctly_classified += number_of_correctly_classified
    result['||hit_rate'] = total_number_of_correctly_classified/N if N not in zero_or_na else None

    confusion_matrix = []
    prediction_labels = all_output_labels
    if cm_include_indecisive:
        prediction_labels.append('INDECISIVE')
    for prediction_label in prediction_labels:
        cm_row = dict()
        for actual_label in all_output_labels:
            cm_row[actual_label] = len(df[(df['predicted_y'] == prediction_label) & (df['actual_y'] == actual_label)])
        confusion_matrix.append(cm_row)
    confusion_matrix = pd.DataFrame(confusion_matrix,index=all_output_labels).sort_index()
    return pd.DataFrame([result]).T,confusion_matrix
