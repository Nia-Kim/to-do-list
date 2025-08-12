from task_create import task_create
from task_update import task_update
from task_read import task_read
from task_delete import task_delete

def main():
    to_do_list = []

    while True:
        print("\n작업 선택")
        print("1. to do 생성")
        print("2. to do 수정")
        print("3. to do 조회")
        print("4. to do 삭제")
        print("5. 작업 종료")
        select_task = input("작업 호출: ")

        if select_task == "1":
            task_create()

        elif select_task == "2":
            task_update()

        elif select_task == "3":
            task_read()
        
        elif select_task == "4":
            task_delete()

        elif select_task == "5":
            print("작업을 종료합니다.")
            break

        else:
            print("작업을 찾을 수 없습니다.")

if __name__ == "__main__":
    main()