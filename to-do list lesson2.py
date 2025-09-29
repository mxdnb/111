tasks = []

def show_tasks():
    if not tasks:
        print("当前没有任务。")
    else:
        for i, task in enumerate(tasks):
            status = "已完成" if task["done"] else "未完成"
            print(f"{i+1}. {task['name']} [{status}]")

def add_task():
    name = input("请输入新任务内容：")
    tasks.append({"name": name, "done": False})
    print("任务已添加。")

def complete_task():
    show_tasks()
    num = int(input("请输入要标记为已完成的任务编号："))
    if 1 <= num <= len(tasks):
        tasks[num-1]["done"] = True
        print("任务已标记为已完成。")
    else:
        print("无效的任务编号。")

while True:
    print("\n1. 添加新任务\n2. 显示所有任务\n3. 标记任务为已完成\n4. 退出")
    choice = input("请选择操作：")
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("再见！")
        break
    else:
        print("无效选择，请重新输入。")
