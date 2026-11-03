import json
p = r"G:\GoProject\package\答案.json"
d = json.load(open(p, encoding="utf-8"))
print("keys", list(d.keys()))
print("name", d["选手名称"], "pkg", d["参赛包编号"], "n", len(d["答案"]))
for tid in ["M015-S001","M069-S001","M077-S009","M078-S009","M081-S011","M090-S008"]:
    q = [x["查询语句"] for x in d["答案"] if x["题号"]==tid][0]
    print("\n"+tid, "->", q)
