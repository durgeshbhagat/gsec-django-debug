from django.shortcuts import render
import pickle
import os
from graphos.sources.simple import SimpleDataSource
from graphos.renderers import gchart




BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DICT_DIR = os.path.join(BASE_DIR, 'script_dir', 'dict_dir')

post_list = ['Vice_President', 'Technical', 'Cultural', 'Sports', 'Welfare', 'HAB']
post_name = ['vp', 'technical', 'cultural', 'sports', 'welfare', 'hab']


# [["Completed" , count], ...]
def draw_chart(post_dict):
    data = []
    data.append(['status', 'No of task'])
    for status, temp_dict in post_dict.items():
        data.append([status, len(temp_dict)])
    # DataSource object
    data_source = SimpleDataSource(data=data)
    # Chart object
    chart = gchart.PieChart(data_source)
    return chart

#auxialliary function
def fetch_dict_file(post_name):
    fname = os.path.join(DICT_DIR, post_name + '.pkl')
    fin = open(fname, 'rb')
    post_dict = pickle.load(fin)
    fin.close()
    fname = os.path.join(DICT_DIR, 'candidate_info' + '.pkl')
    fin = open(fname, 'rb')
    candidate_info = pickle.load(fin)
    fin.close()
    return post_dict, candidate_info[post_name]


def vp(request):
    post_dict, candidate_info = fetch_dict_file(post_name[0])
    template_name = 'gsecWorkStatus/{0}.html'.format(post_list[0])
    chart = draw_chart(post_dict)
    return render(request, template_name, {'post_dict': post_dict, 'candidate_info': candidate_info, 'pie_chart' : chart,
                                           })


def technical(request):
    post_dict, candidate_info = fetch_dict_file(post_name[1])
    template_name = 'gsecWorkStatus/{0}.html'.format(post_list[1])
    chart = draw_chart(post_dict)
    return render(request, template_name, {'post_dict': post_dict, 'candidate_info': candidate_info, 'pie_chart' : chart,
                                           })


def cultural(request):
    post_dict, candidate_info = fetch_dict_file(post_name[2])
    template_name = 'gsecWorkStatus/{0}.html'.format(post_list[2])
    chart = draw_chart(post_dict)
    return render(request, template_name, {'post_dict': post_dict, 'candidate_info': candidate_info, 'pie_chart' : chart,
                                           })


def sports(request):
    post_dict, candidate_info = fetch_dict_file(post_name[3])
    template_name = 'gsecWorkStatus/{0}.html'.format(post_list[3])
    chart = draw_chart(post_dict)
    return render(request, template_name, {'post_dict': post_dict, 'candidate_info': candidate_info, 'pie_chart' : chart,
                                           })


def welfare(request):
    post_dict, candidate_info = fetch_dict_file(post_name[4])
    template_name = 'gsecWorkStatus/{0}.html'.format(post_list[4])
    chart = draw_chart(post_dict)
    return render(request, template_name, {'post_dict': post_dict, 'candidate_info': candidate_info, 'pie_chart' : chart,
                                           })


def hab(request):
    post_dict, candidate_info = fetch_dict_file(post_name[5])
    template_name = 'gsecWorkStatus/{0}.html'.format(post_list[5])
    chart = draw_chart(post_dict)
    return render(request, template_name, {'post_dict': post_dict, 'candidate_info': candidate_info, 'pie_chart' : chart,
                                           })
