import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

data_map = {
    'NHBE': {
        'healthy': ['Series1_NHBE_Mock_1', 'Series1_NHBE_Mock_2', 'Series1_NHBE_Mock_3', 'Series9_NHBE_Mock_1',
                    'Series9_NHBE_Mock_2', 'Series9_NHBE_Mock_3', 'Series9_NHBE_Mock_4'],
        'sars-cov2': ['Series1_NHBE_SARS-CoV-2_1', 'Series1_NHBE_SARS-CoV-2_2', 'Series1_NHBE_SARS-CoV-2_3'],
        'iav': ['Series9_NHBE_IAV_1', 'Series9_NHBE_IAV_2', 'Series9_NHBE_IAV_3', 'Series9_NHBE_IAV_4'],
        'iavdns1': ['Series9_NHBE_IAVdNS1_1', 'Series9_NHBE_IAVdNS1_2', 'Series9_NHBE_IAVdNS1_3',
                    'Series9_NHBE_IAVdNS1_4'],
        'ifnb_treated': ['Series9_NHBE_IFNB_4h_1', 'Series9_NHBE_IFNB_4h_2', 'Series9_NHBE_IFNB_6h_1',
                         'Series9_NHBE_IFNB_6h_2', 'Series9_NHBE_IFNB_12h_1', 'Series9_NHBE_IFNB_12h_2']
    },
    'A549': {
        'healthy': ['Series2_A549_Mock_1', 'Series2_A549_Mock_2', 'Series2_A549_Mock_3', 'Series3_A549_Mock_1',
                    'Series3_A549_Mock_2', 'Series4_A549_Mock_1', 'Series4_A549_Mock_2', 'Series5_A549_Mock_1',
                    'Series5_A549_Mock_2', 'Series5_A549_Mock_3', 'Series8_A549_Mock_1', 'Series8_A549_Mock_2',
                    'Series8_A549_Mock_3'],
        'sars-cov2': ['Series2_A549_SARS-CoV-2_1', 'Series2_A549_SARS-CoV-2_2', 'Series2_A549_SARS-CoV-2_3',
                      'Series5_A549_SARS-CoV-2_1', 'Series5_A549_SARS-CoV-2_2', 'Series5_A549_SARS-CoV-2_3'],
        'iav': ['Series4_A549_IAV_1', 'Series4_A549_IAV_2'],
        'rsv': ['Series3_A549_RSV_1', 'Series3_A549_RSV_2'],
        'hpiv3': ['Series8_A549_HPIV3_3', 'Series8_A549_HPIV3_2', 'Series8_A549_HPIV3_1'],
        'healthy_ace2': ['Series6_A549-ACE2_Mock_1', 'Series6_A549-ACE2_Mock_2', 'Series6_A549-ACE2_Mock_3',
                         'Series16_A549-ACE2_Mock_1', 'Series16_A549-ACE2_Mock_2', 'Series16_A549-ACE2_Mock_3'],
        'sars-cov2_ace2': ['Series6_A549-ACE2_SARS-CoV-2_1', 'Series6_A549-ACE2_SARS-CoV-2_2',
                           'Series6_A549-ACE2_SARS-CoV-2_3', 'Series16_A549-ACE2_SARS-CoV-2_1',
                           'Series16_A549-ACE2_SARS-CoV-2_2', 'Series16_A549-ACE2_SARS-CoV-2_3'],
        'sars-cov2_ace2_rux': ['Series16_A549-ACE2_SARS-CoV-2_Rux_1', 'Series16_A549-ACE2_SARS-CoV-2_Rux_2',
                               'Series16_A549-ACE2_SARS-CoV-2_Rux_3']
    },
    'Calu3': {
        'healthy': ['Series7_Calu3_Mock_1', 'Series7_Calu3_Mock_2', 'Series7_Calu3_Mock_3'],
        'sars-cov2': ['Series7_Calu3_SARS-CoV-2_1', 'Series7_Calu3_SARS-CoV-2_2', 'Series7_Calu3_SARS-CoV-2_3']
    },
    'biopsy': {
        'healthy': ['Series15_HealthyLungBiopsy_2', 'Series15_HealthyLungBiopsy_1'],
        'sars-cov2': ['Series15_COVID19Lung_2', 'Series15_COVID19Lung_1']
    }
}

ferret_data_map = {
    'nasal_wash': {
        'healthy_day1': ['Series10_FerretNW_Ctl_d1_1', 'Series10_FerretNW_Ctl_d1_2'],
        'sars-cov2_day1': ['Series10_FerretNW_SARS-CoV-2_d1_1', 'Series10_FerretNW_SARS-CoV-2_d1_2'],
        'healthy_day3': ['Series11_FerretNW_Ctl_d3_1', 'Series11_FerretNW_Ctl_d3_2'],
        'sars-cov2_day3': ['Series11_FerretNW_SARS-CoV-2_d3_1', 'Series11_FerretNW_SARS-CoV-2_d3_2'],
        'healthy_day7': ['Series12_FerretNW_Ctl_d7_1', 'Series12_FerretNW_Ctl_d7_2'],
        'sars-cov2_day7': ['Series12_FerretNW_SARS-CoV-2_d7_1', 'Series12_FerretNW_SARS-CoV-2_d7_2'],
        'healthy_day14': ['Series13_FerretNW_Ctl_d14_1', 'Series13_FerretNW_Ctl_d14_2'],
        'sars-cov2_day14': ['Series13_FerretNW_SARS-CoV-2_d14_1', 'Series13_FerretNW_SARS-CoV-2_d14_2'],
    },
    'trachea': {
        'healthy_day3': ['Series14_FerretTrachea_Ctl_d3_1', 'Series14_FerretTrachea_Ctl_d3_2',
                         'Series14_FerretTrachea_Ctl_d3_3', 'Series14_FerretTrachea_Ctl_d3_4'],
        'iav_day3': ['Series14_FerretTrachea_IAV_d3_3', 'Series14_FerretTrachea_IAV_d3_5',
                     'Series14_FerretTrachea_IAV_d3_2', 'Series14_FerretTrachea_IAV_d3_1',
                     'Series14_FerretTrachea_IAV_d3_4', 'Series14_FerretTrachea_IAV_d3_6'],
        'sars-cov2_day3': ['Series14_FerretTrachea_SARS-CoV-2_d3_1', 'Series14_FerretTrachea_SARS-CoV-2_d3_2',
                           'Series14_FerretTrachea_SARS-CoV-2_d3_3', 'Series14_FerretTrachea_SARS-CoV-2_d3_4']
    }
}

__dataInterpreter_data = pd.read_csv('data/GSE147507_RawReadCounts_Human.tsv', index_col=0, sep='\t')
__dataInterpreter_ferret_data = pd.read_csv('data/GSE147507_RawReadCounts_Ferret.tsv', index_col=0, sep='\t')


################################
#                              #
#   Data Gathering Functions   #
#                              #
################################

def get_columns(cell_type, *treatments, series=None, ferret=False):
    columns = []

    if not ferret:
        for treatment in treatments:
            columns += data_map[cell_type][treatment]
    else:
        for treatment in treatments:
            columns += ferret_data_map[cell_type][treatment]

    if series is not None:
        res = []
        for s in series:
            res += [col for col in columns if 'Series' + str(s) + '_' in col]

        return res

    return columns


def get_data(cell_type, *treatments, series=None, ferret=False, apply_log=True, remove_zeros=True):
    if not ferret:
        result = __dataInterpreter_data[get_columns(cell_type, *treatments, series=series, ferret=ferret)].copy()
    else:
        result = __dataInterpreter_ferret_data[get_columns(cell_type, *treatments, series=series, ferret=ferret)].copy()

    if apply_log:
        result = np.log(result + 1)

    if remove_zeros:
        result = result.loc[(result != 0).any(axis=1)]

    return result


def get_data_by_series(series, apply_log=True, remove_zeros=True):
    result = __dataInterpreter_data.filter(like="Series" + str(series) + "_").copy()

    if apply_log:
        result = np.log(result + 1)

    if remove_zeros:
        result = result.loc[(result != 0).any(axis=1)]

    return result


################################
#                              #
#      Modeling Functions      #
#                              #
################################

def welch(v1, v2):
    return scipy.stats.ttest_ind(v1, v2, equal_var=True).pvalue


def ttest(v1, v2):
    return scipy.stats.ttest_ind(v1, v2).pvalue


def mannwhitneyu(v1, v2):
    return scipy.stats.mannwhitneyu(v1, v2).pvalue


__dataInterpreter_t_test_options = {
    'welch': welch,
    't-test': ttest,
    'mannwhitneyu': mannwhitneyu
}


def get_p_values(test, data, set1, set2, limit=0.05):
    pvalues = []

    for index, row in data.iterrows():
        pvalues += [__dataInterpreter_t_test_options[test](row[set1], row[set2])]

    data.insert(len(data.columns), "p-value", pvalues)

    return data.loc[data['p-value'] < limit]


def plot_dendrogram(data):
    fig = plt.figure(figsize=(25, 10))
    dendrogram = sch.dendrogram(sch.linkage(data, method="ward"))
    plt.title('Dendrogram')
    plt.xlabel('Genes')
    plt.ylabel('Distances')
    plt.show()
