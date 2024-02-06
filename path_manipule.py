import os

def get_pure_base_name(path):
    head, tail = os.path.split(path)
    base_name, Extension = tail.split('.')
    return head, base_name, Extension

def append_to_base_name(path, append_to_name):
    head, base_name, Extension = get_pure_base_name(path)
    a = os.path.join(head, base_name + append_to_name + '.' + Extension)
    print(a)
    return a

# a = ["sdfsdf/dsfs/fsd/dd.t", "dfsd\\sdf\\fs\\d.yt", "sdfwre\werw\wer.u", "dsfksjg//fdgsg//sdgg.po"]
# for i in a:
#     print(append_to_base_name(i, "merd"))