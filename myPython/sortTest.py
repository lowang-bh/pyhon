import operator
import re


class test(object):
    def __init__(self):
        self._key = 1

    def __nonzero__(self):
        print("__nonzero__")
        if self._key:
            return True
        else:
            return False


t = test()
if t:
    print(t)

target = {'10.143.248.34': [43.254, 30, 742.263, 284.677],
          '10.143.248.15': [41.079, 0, 1687.174, 685.617],
          '10.143.248.33': [43.254, 40, 742.263, -2104.677],
          '10.143.248.100': [43.254, 40, 520.29, -1528.130],
          '10.143.248.23': [182.882, 30, 2816.796, 966.407],
          '10.143.248.24': [179.402, 0, 2796.753, 1050.882],
          '10.143.248.22': [117.484, 0, 2963.993, 549.40]}

sortedlist = sorted(target.iteritems(), key=lambda (k, v): operator.itemgetter(0, 1, 2)(v), reverse=True)
print(sortedlist)
for item in sortedlist:
    print(item)

print(target)
print("another way")
sortedlist = sorted(target.iteritems(), key=lambda x: (x[1][0], x[1][1], x[1][2]), reverse=True)
for item in sortedlist:
    print(item)

gameresult = [{'losses': 3, 'name': 'Bob', 'rating': 75.0, 'wins': 10},
              {'losses': 5, 'name': 'David', 'rating': 57.0, 'wins': 3},
              {'losses': 5, 'name': 'Carol', 'rating': 57.0, 'wins': 4},
              {'losses': 3, 'name': 'Patty', 'rating': 71.48, 'wins': 9}]

for item in sorted(gameresult, key=lambda x: (x["rating"], x["name"])):
    print(item)

print(sorted(gameresult, key=operator.itemgetter("rating", "name")))


def generate_vmname_key(role, cluster):
    """
    :param role: role name
    :param cluster: cluster name
    :return: 
    """
    if role == "jenkins":
        key = "sa-jenkins-k8s"
    elif role == "etcd":
        key = "sa-etcd-" + cluster
    else:  # other roles: node, master, ingress, etc
        key = "sa-k8s-" + cluster
    return key


sorted_servers = [('10.143.248.24', [186.189, 253.3415, 2794.968, 1050.882]),
                  ('10.143.248.23', [182.876, 289.3415, 2816.796, 966.407]),
                  ('10.143.248.22', [117.259, 151.496, 2963.993, 549.407]),
                  ('10.143.248.15', [41.078, 73.362, 1687.174, 685.617]),
                  ('10.143.248.34', [40.832, -14.349, 726.371, -1284.677]),
                  ('10.143.248.100', [26.602, 47.965, 520.29, -1528.130]),
                  ('10.143.248.33', [17.787, -94.115, 742.263, -2104.677])]

sorted_servers = [('10.143.248.24', [184.34, 221.341, 2792.95, 810.883, 95.561])
                  ('10.143.248.23', [182.848, 289.341, 2816.796, 966.407, 163.561])
                  ('10.143.248.22', [118.264, 159.497, 2962.312, 549.408, 65.214])
                  ('10.143.248.15', [41.083, 73.363, 1687.174, 685.618, 42.075])
                  ('10.143.248.34', [39.761, -14.349, 727.999, -844.677, -77.134])
                  ('10.143.248.100', [26.497, 47.966, 520.29, -1528.131, 16.644])
                  ('10.143.248.33', [11.371, -86.115, 738.385, -1904.677, -148.978])]

sorted_server2 = [('10.143.248.23', [163.561, 182.845, 289.341, 2816.796, 966.407])
                  ('10.143.248.24', [95.561, 184.341, 221.341, 2792.95, 810.883])
                  ('10.143.248.22', [65.214, 118.245, 159.497, 2962.312, 549.408])
                  ('10.143.248.15', [42.075, 41.089, 73.363, 1687.174, 685.618])
                  ('10.143.248.100', [16.644, 26.508, 47.966, 520.29, -1528.131])
                  ('10.143.248.34', [-77.134, 39.755, -14.349, 727.999, -844.677])
                  ('10.143.248.33', [-148.978, 11.37, -86.115, 738.385, -1904.677])]

vm_key = generate_vmname_key("ingress", "xyz")
nums_list = []

# vmlist = ['kvm24-sa-k8s-test7', 'kvm22-sa-k8s-test8', 'kvm23-sa-k8s-test9', 'kvm24-sa-k8s-test10',
#           'kvm23-sa-k8s-test1', 'kvm24-sa-k8s-test2', 'kvm24-sa-k8s-test4', 'kvm23-sa-k8s-test3', 'kvm23-sa-k8s-test5',
#           'kvm24-sa-k8s-test6']


vmlist = ['kvm100-sa-k8s-xyz7', 'kvm23-sa-k8s-xyz14', 'kvm24-sa-k8s-xyz15', 'kvm24-sa-k8s-xyz16', 'kvm23-sa-k8s-xyz17',
          'kvm22-sa-k8s-xyz5', 'kvm33-sa-k8s-xyz100', 'kvm33-sa-k8s-xyz101', 'kvm34-sa-k8s-xyz102',
          'kvm34-sa-k8s-xyz103', 'kvm33-sa-k8s-xyz18', 'kvm33-sa-k8s-xyz19', 'kvm33-sa-k8s-xyz20', 'kvm34-sa-k8s-xyz21',
          'kvm34-sa-k8s-xyz22']
myreg = re.compile(r'%s([0-9]+)' % vm_key)
for vm_name in vmlist:
    res = myreg.search(vm_name)
    if res:
        print res.group(), res.group(1)
        nums_list.append(int(res.group(1)))

print(nums_list)
print(max(nums_list), min(nums_list))

ipslits = str.split("10.143.248.0", ".")[0:3]
ipprefix = ".".join(str.split("10.143.248.0", ".")[0:3])
ignore_ips = [ipprefix + ".0", ipprefix + ".255"]
print(ignore_ips)

print(float("%.3F" % (1024 / 3.0)))
print(83.425 + 101.109)
print("{0:.3f}".format(3.14159))
