from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def index():
    return render_template("index.html")

@views.route("/python_introduction")
def introduction():
    return render_template("python_pages/introduction.html")

@views.route("/python_decision_making")
def decision_making():
    return render_template("python_pages/decision_making.html")

@views.route("/python_dictionaries")
def dictionaries():
    return render_template("python_pages/dictionaries.html")

@views.route("/python_functions")
def functions():
    return render_template("python_pages/functions.html")

@views.route("/python_lists")
def lists():
    return render_template("python_pages/lists.html")

@views.route("/python_loops")
def loops():
    return render_template("python_pages/loops.html")

@views.route("/python_more_projects")
def more_projects():
    return render_template("python_pages/more_projects.html")

@views.route("/python_object_oriented_programming")
def object_oriented_programming():
    return render_template("python_pages/object_oriented_programming.html")

@views.route("/python_projects")
def projects():
    return render_template("python_pages/projects.html")

@views.route("/python_solutions")
def solutions():
    return render_template("python_pages/solutions.html")

@views.route("/python_working_with_files")
def working_with_files():
    return render_template("python_pages/working_with_files.html")

@views.route("/download_page")
def download_page():
    # documents = [
    # {'name': 'ASL_00 Projects and KSBs', 'image': 'ASL_00.png'},
    # {'name': 'ASL_01 Fundamentals of Application Support', 'image': 'ASL_01.jpg'},
    # {'name': 'ASL_02 Introduction to Service Management', 'image': 'ASL_02.png'},
    # {'name': 'ASL_03 Agile & Teamwork', 'image': 'ASL_03.jpg'},
    # {'name': 'ASL_04 Users, Customers and Stakeholders', 'image': 'ASL_04.png'},
    # {'name': 'ASL_05 Security in Applications', 'image': 'ASL_05.png'},
    # {'name': 'ASL_06 Applying security in Applications', 'image': 'ASL_06.png'},
    # {'name': 'ASL_07 DevOps in Application Support', 'image': 'ASL_07.png'},
    # {'name': 'ASL_08 Data in Application Support', 'image': 'ASL_08.png'},
    # {'name': 'ASL_09 Working with Data in Application Support', 'image': 'ASL_09.png'},
    # {'name': 'ASL_10 Testing', 'image': 'ASL_10.png'},
    # {'name': 'ASL_11 Production & Live Support', 'image': 'ASL_11.jpg'},
    # {'name': 'ASL_12 Defect Management', 'image': 'ASL_12.png'},
    # {'name': 'ASL_13 Bringing it all Together', 'image': 'ASL_13.png'},
    # {'name': 'ASL_14 Career Development & Onward Progression', 'image': 'ASL_14.png'},
    # {'name': 'ASL_15 Useful stuff', 'image': 'ASL_15.jpg'}]
    return render_template("download_page.html")
    # documents = [
    # {'name': 'ASL05 Day 1', 'file': 'ASL05/ASL05 - Security in Applications Day1.pptx'},
    # {'name': 'ASL05 Day 2', 'file': 'ASL05/ASL05 - Security in Applications Day2.pptx'},
    # {'name': 'ASL05 Day 2', 'file': 'ASL05/TEST.TXT'}]
    # return render_template("download_pages/asl05_download_page.html", documents=documents)

@views.route("/download/asl00")
def asl00_download_page():
    return render_template("download_pages/asl00_download_page.html")

@views.route("/download/asl01")
def asl01_download_page():
    return render_template("download_pages/asl01_download_page.html")

@views.route("/download/asl02")
def asl02_download_page():
    return render_template("download_pages/asl02_download_page.html")

@views.route("/download/asl03")
def asl03_download_page():
    return render_template("download_pages/asl03_download_page.html")

@views.route("/download/asl04")
def asl04_download_page():
    return render_template("download_pages/asl04_download_page.html")

@views.route("/download/asl05")
def asl05_download_page():
    return render_template("download_pages/asl05_download_page.html")

@views.route("/download/asl06")
def asl06_download_page():
    return render_template("download_pages/asl06_download_page.html")

@views.route("/download/asl07")
def asl07_download_page():
    return render_template("download_pages/asl07_download_page.html")

@views.route("/download/asl08")
def asl08_download_page():
    return render_template("download_pages/asl08_download_page.html")

@views.route("/download/asl09")
def asl09_download_page():
    return render_template("download_pages/asl09_download_page.html")

@views.route("/download/asl10")
def asl10_download_page():
    return render_template("download_pages/asl10_download_page.html")

@views.route("/download/asl11")
def asl11_download_page():
    return render_template("download_pages/asl11_download_page.html")

@views.route("/download/asl12")
def asl12_download_page():
    return render_template("download_pages/asl12_download_page.html")

@views.route("/download/asl13")
def asl13_download_page():
    return render_template("download_pages/asl13_download_page.html")

@views.route("/download/asl14")
def asl14_download_page():
    return render_template("download_pages/asl14_download_page.html")

@views.route("/download/asl15")
def asl15_download_page():
    return render_template("download_pages/asl15_download_page.html")

@views.route("/sql_introduction")
def sql_introduction():
    return render_template("sql_pages/introduction.html")

@views.route("/sql_sql_fundamentals")
def sql_sql_fundamentals():
    return render_template("sql_pages/sql_fundamentals.html")

@views.route("/sql_data_manipulation")
def sql_data_manipulation():
    return render_template("sql_pages/data_manipulation.html")

@views.route("/sql_filtering_and_sorting")
def sql_filtering_and_sorting():
    return render_template("sql_pages/filtering_and_sorting.html")

@views.route("/linux_introduction")
def linux_introduction():
    return render_template("linux_pages/introduction.html")
