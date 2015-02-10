#-*- coding: utf8 -*-
from multiprocessing.pool import ThreadPool as Pool
from multiprocessing import cpu_count

pool_size = 2 #cpu_count()
if pool_size < 0:
    pool_size = cpu_count()

print 'Number of CPUs = ' + str(cpu_count())
print 'poll size = ' + str(pool_size)
case_length = 10
xml_cases_dic = {}

def process_xml_gen(case, idx):
    xml_case = case
    if xml_case == None:
        raise 'XML Generation Exception.'

    xml_cases_dic[idx] = xml_case

    print 'Complete Index: ' + str(idx)

    return True


pool = Pool(processes=pool_size)

# Generation 수행
for case_count, case in enumerate(range(0, case_length)):
    pool.apply_async(process_xml_gen, (case*2, case_count))

pool.close()
pool.join()

print xml_cases_dic
print xml_cases_dic[0]
xml_cases = []
# Convert dictionary to list
for xml_idx in range(case_length):
    print 'try : %d' % xml_idx
    print xml_cases_dic[xml_idx]
    xml_cases.extend(xml_cases_dic[xml_idx])


print xml_cases