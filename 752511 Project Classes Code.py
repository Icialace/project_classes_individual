from tabulate import tabulate

# Doctor Class and Functions
class Doctor:
  def formatDrInfo(new_doctor):
    new_doctor_info = '_'.join(new_doctor)
    new_doctor_info = "\n" + new_doctor_info
    return new_doctor_info
  
  def enterDrInfo():
    new_doctor = []
    new_doctor.append(input("Enter the ID of the new doctor: "))
    new_doctor.append(input("Enter the doctor's name: "))
    new_doctor.append(input("Enter the doctor's specialization: "))
    new_doctor.append(input("Enter the doctor's work hours(e,g, 7AM-10PM): "))
    new_doctor.append(input("Enter the doctor's qualifications: "))
    new_doctor.append(input("Enter the doctor's room number: "))
    print("\n")
    return new_doctor
  
  def readDoctorsFile():
    with open("/content/doctors.txt", mode = "r") as doctor_open:
      doctor_raw_data = doctor_open.readlines()
    return doctor_raw_data

  def searchDoctorByID(doctor_raw_data):
    doctor_id = input('Enter Doctor ID: ')
    doctor_id = doctor_id + ":"
    print("\n")
    doctor_search = []
    headers = "Specialization"
    for line in doctor_raw_data:
      line = line.replace('_', ':')
      if line.find(headers) != -1:
        doctor_search.append(line)
    for line in doctor_raw_data:
      line = line.replace('_', ':')
      if line.startswith(doctor_id) == True:
        doctor_search.append(line)
    for line in doctor_raw_data:
      line = line.replace('_', ':')
      if line.startswith(doctor_id) == False:
        doctor_search.append("0")
    return doctor_search
  
  def searchDoctorByName(doctor_raw_data):
    word = input("Enter the doctor's name: ")
    word = word + ":"
    print("\n")
    doctor_search = []
    headers = "Specialization"
    for line in doctor_raw_data:
      line = line.replace('_', ':')
      if line.find(headers) != -1:
        doctor_search.append(line)
    for line in doctor_raw_data:
      line = line.replace('_', ':')
      if line.find(word) != -1:
        doctor_search.append(line)
    for line in doctor_raw_data:
      line = line.replace('_', ':')
      if line.find(word) == -1:
        doctor_search.append("1")
    return doctor_search
  
  def displayDoctorInfo(doctor_search_input):
      doctor_search = doctor_search_input[0].strip('\n').split(':'), doctor_search_input[1].strip('\n').split(':')
      if doctor_search_input[1] == "0":
        print("This doctor's ID does not exist in the system\n")
      elif doctor_search_input[1] == "1":
        print("This doctor's name does not exist in the system\n")
      else:
        print(tabulate(doctor_search, headers = 'firstrow'), "\n")

  def editDoctorInfo():
    edit_doctor = []
    edit_doctor_id = input("Enter the ID of the doctor who's information you would like to edit: ")
    edit_doctor.append(edit_doctor_id)
    edit_doctor.append(input("Enter new doctor's name: "))
    edit_doctor.append(input("Enter new doctor's specialization: "))
    edit_doctor.append(input("Enter new doctor's work hours(e,g, 7AM-10PM): "))
    edit_doctor.append(input("Enter new doctor's qualification: "))
    edit_doctor.append(input("Enter new doctor's room number: "))
    print("\n")
    doctor_edited = '_'.join(edit_doctor)
    doctor_edited = doctor_edited + "\n"
    with open("/content/doctors.txt", mode = "r") as doctor_open:
      doctor_raw_data = doctor_open.readlines()
      doctor_list = []
      for line in doctor_raw_data:
        if line.startswith(edit_doctor_id) == True:
          doctor_list.append(doctor_edited)
        elif line.startswith(edit_doctor_id) == False:
          doctor_list.append(line)
    with open("/content/doctors.txt", mode = "w") as doctor_write:
      for line in doctor_list:
        doctor_write.write(line)
  
  def displayDoctorsList(doctor_raw_data):
    doctor_data = []
    for line in doctor_raw_data:
      doctor_list = line.strip('\n').split('_')
      doctor_data.append(doctor_list)
    print(tabulate(doctor_data, headers = "firstrow"), "\n")
    print("Returning Back to Previous Menu\n")
  
  def writeListOfDoctorsToFile(list_of_doctors):
    doctor_write_list = []
    for line in list_of_doctors:
      new_doctor_info = line.split(" ")
      new_doctor_info = "_".join(new_doctor_info)
      doctor_write_list.append(new_doctor_info)
    with open("/content/doctors.txt", mode = "a") as doctor_write:
      doctor_write.write("\n")
      for line in doctor_write_list:
        doctor_write.write(line)
  
  def addDrToFile(new_doctor_info):
    with open("/content/doctors.txt", mode = "a") as doctor_open:
      doctor_open.write(new_doctor_info)

# Facility Class and Functions
class Facility:
  def addFacility():
    added_facility = input("Enter Facility Name: ")
    added_facility =  "\n" + added_facility
    with open("/content/facilities.txt", mode = "a") as facilities_write:
      facilities_write.write(added_facility)
    print("\n")
  
  def displayFacilities():
    with open("/content/facilities.txt", mode = "r") as facilities_open:
      facilities_raw_data = facilities_open.readlines()
      facilities_data = []
      for line in facilities_raw_data:
        facilities_list = line.split("\n")
        facilities_data.append(facilities_list)
      print(tabulate(facilities_data, headers = "firstrow"), "\n")
  
  def writeListOfFacilitiesToFile(list_of_facilities):
    facility_write_list = []
    for line in list_of_facilities:
      new_facility_info = line.split(" ")
      new_facility_info = "_".join(new_facility_info)
      facility_write_list.append(new_facility_info)
    with open("/content/facilities.txt", mode = "a") as facility_write:
      facility_write.write("\n")
      for line in facility_write_list:
        facility_write.write(line)

# Laboratory Class and Functions
class Laboratory:
  def addLabToFile(new_lab_info):
    with open("/content/laboratories.txt", mode = "a") as lab_open:
      lab_open.write(new_lab_info)
  
  def writeListOfLabsToFile(list_of_labs):
    lab_write_list = []
    for line in list_of_labs:
      new_lab_info = line.split(" ")
      new_lab_info = "_".join(new_lab_info)
      lab_write_list.append(new_lab_info)
    with open("/content/laboratories.txt", mode = "a") as lab_write:
      lab_write.write("\n")
      for line in lab_write_list:
        lab_write.write(line)
  
  def displayLabsList(lab_raw_data):
    lab_data = []
    for line in lab_raw_data:
      lab_list = line.strip('\n').split('_')
      lab_data.append(lab_list)
    print(tabulate(lab_data, headers = "firstrow"), "\n")
  
  def formatLabInfo(new_lab):
    new_lab_info = '_'.join(new_lab)
    new_lab_info = "\n" + new_lab_info
    return new_lab_info
  
  def enterLabInfo():
    new_lab = []
    new_lab.append(input("Lab name: "))
    new_lab.append("$" + input("Lab cost(e.g., for $800, enter 800): "))
    return new_lab
  
  def readLabFile():
    with open("/content/laboratories.txt", mode = "r") as lab_open:
      lab_raw_data = lab_open.readlines()
    return lab_raw_data

# Patient Class and Functions
class Patient: 
  def formatPatientInfo(new_patient):
    new_patient_info = '_'.join(new_patient)
    new_patient_info = "\n" + new_patient_info
    return new_patient_info
  
  def enterPatientInfo():
    new_patient = []
    new_patient.append(input("New patient's ID: "))
    new_patient.append(input("New patient's name: "))
    new_patient.append(input("New patient's disease: "))
    new_patient.append(input("New patient's gender: "))
    new_patient.append(input("New patient's age: "))
    return new_patient
  
  def readPatientsFile():
    with open("/content/patients.txt", mode = "r") as patient_open:
      patient_raw_data = patient_open.readlines()
    return patient_raw_data
  
  def SearchPatientByID(patient_raw_data):
    patient_id = input("Enter patient's ID: ")
    patient_id = patient_id + ":"
    print("\n")
    patient_search = []
    headers = "Disease"
    for line in patient_raw_data:
      line = line.replace('_', ':')
      if line.find(headers) != -1:
        patient_search.append(line)
    for line in patient_raw_data:
      line = line.replace('_', ':')
      if line.startswith(patient_id) == True:
        patient_search.append(line)
    for line in patient_raw_data:
      line = line.replace('_', ':')
      if line.startswith(patient_id) == False:
        patient_search.append("0")
    return patient_search
  
  def displayPatientInfo(patient_search_input):
      patient_search = patient_search_input[0].strip('\n').split(':'), patient_search_input[1].strip('\n').split(':')
      if patient_search_input[1] == "0":
        print("This patient's ID does not exist in the system\n")
      else:
        print(tabulate(patient_search, headers = 'firstrow'), "\n")
  
  def editPatientInfo():
    edit_patient = []
    edit_patient_id = input("Enter the ID of the patient who's information you would like to edit: ")
    edit_patient.append(edit_patient_id)
    edit_patient.append(input("Enter new patient's name: "))
    edit_patient.append(input("Enter new patient's disease: "))
    edit_patient.append(input("Enter new patient's gender: "))
    edit_patient.append(input("Enter new patient's age: "))
    print("\n")
    patient_edited = '_'.join(edit_patient)
    patient_edited = patient_edited + "\n"
    with open("/content/patients.txt", mode = "r") as patient_open:
      patient_raw_data = patient_open.readlines()
      patient_list = []
      for line in patient_raw_data:
        if line.startswith(edit_patient_id) == True:
          patient_list.append(patient_edited)
        elif line.startswith(edit_patient_id) == False:
          patient_list.append(line)
    with open("/content/patients.txt", mode = "w") as patient_write:
      for line in patient_list:
        patient_write.write(line)
  
  def displayPatientsList(patient_raw_data):
    patient_data = []
    for line in patient_raw_data:
      patient_list = line.strip('\n').split('_')
      patient_data.append(patient_list)
    print(tabulate(patient_data, headers = "firstrow"), "\n")
  
  def writeListOfPatientsToFile(list_of_patients):
    patient_write_list = []
    for line in list_of_patients:
      new_patient_info = line.split(" ")
      new_patient_info = "_".join(new_patient_info)
      patient_write_list.append(new_patient_info)
    with open("/content/patients.txt", mode = "a") as patient_write:
      patient_write.write("\n")
      for line in patient_write_list:
        patient_write.write(line)
  
  def addPatienttoFile(new_patient_info):
    with open("/content/patients.txt", mode = "a") as patient_open:
      patient_open.write(new_patient_info)

# Management Class and Functions
class Management:
  def DisplayMenu():
    choice = input("Welcome to Alberta Hospital (AH) Management System.\n\
    please select from the following options, or select 0 to stop:\n\
    1 - Doctors\n\
    2 - Facilities\n\
    3 - Laboratories\n\
    4 - Patients\n")
    return choice
  
  def DoctorMenu():
    choose_doctor = input("Doctors Menu\n\
    1 - Display Doctors List\n\
    2 - Search for Doctor by ID\n\
    3 - Search for Doctor By Name\n\
    4 - Add Doctor\n\
    5 - Edit Doctor Info\n\
    6 - Back to the Main Menu\n")
    return choose_doctor

  def LabMenu():
    choose_lab = input("Laboratory Menu\n\
    1 - Display Laboratories List\n\
    2 - Add Laboratory\n\
    3 - Back to the Main Menu\n")
    return choose_lab

  def FacilityMenu():
    choose_facility = input("Facilities Menu\n\
    1 - Display Facilities List\n\
    2 - Add Facility\n\
    3 - Back to the Main Menu\n")
    return choose_facility

  def PatientMenu():
    choose_patient = input("Patients Menu\n\
    1 - Display Patients List\n\
    2 - Search for Patient by ID\n\
    3 - Add Patient\n\
    4 - Edit Patient Info\n\
    5 - Back to main Menu\n")
    return choose_patient

choice = "x"
while choice != "0":
  choice = Management.DisplayMenu()
  if choice == "1":
    choose_doctor = "0"
    while choose_doctor != "6":
      choose_doctor = Management.DoctorMenu()
      if choose_doctor == "1":
        read_doctor = Doctor.readDoctorsFile()
        Doctor.displayDoctorsList(read_doctor)
      elif choose_doctor == "2":
        read_doctor = Doctor.readDoctorsFile()
        doctor_search = Doctor.searchDoctorByID(read_doctor)
        Doctor.displayDoctorInfo(doctor_search)
      elif choose_doctor == "3":
        read_doctor = Doctor.readDoctorsFile()
        doctor_search = Doctor.searchDoctorByName(read_doctor)
        Doctor.displayDoctorInfo(doctor_search)
      elif choose_doctor == "4":
        new_doctor = Doctor.enterDrInfo()
        format_new_doctor = Doctor.formatDrInfo(new_doctor)
        Doctor.addDrToFile(format_new_doctor)
      elif choose_doctor == "5":
        Doctor.editDoctorInfo()
      elif choose_doctor == "6":
        print("Returning to Previous Menu\n")
      else:
        choose_doctor = "x"
        print("Error! Please Try Again!0\n")
  elif choice == "2":
    choose_facility = "0"
    while choose_facility != "3":
      choose_facility = Management.FacilityMenu()
      if choose_facility == "1":
        Facility.displayFacilities()
      elif choose_facility == "2":
        Facility.addFacility()
      elif choose_facility == "3":
        print("Returning to Previous Menu\n")
      else:
        choose_facility = "x"
        print("Error! Please Try Again!\n")
  elif choice == "3":
    choose_lab = "0"
    while choose_lab != "3":
      choose_lab = Management.LabMenu()
      if choose_lab == "1":
        lab_read = Laboratory.readLabFile()
        Laboratory.displayLabsList(lab_read)
      elif choose_lab == "2":
        new_lab = Laboratory.enterLabInfo()
        format_new_lab = Laboratory.formatLabInfo(new_lab)
        Laboratory.addLabToFile(format_new_lab)
      elif choose_lab == "3":
        print("Returning to Previous Menu\n")
      else:
        choose_lab = "x"
        print("Error! Please Try Again!\n")
  elif choice == "4":
    choose_patient = "0"
    while choose_patient != "5":
      choose_patient = Management.PatientMenu()
      if choose_patient == "1":
        patient_read = Patient.readPatientsFile()
        Patient.displayPatientsList(patient_read)
      elif choose_patient == "2":
        patient_read = Patient.readPatientsFile()
        search_patient = Patient.SearchPatientByID(patient_read)
        Patient.displayPatientInfo(search_patient)
      elif choose_patient == "3":
        new_patient = Patient.enterPatientInfo()
        format_new_patient = Patient.formatPatientInfo(new_patient)
        Patient.addPatienttoFile(format_new_patient)
      elif choose_patient == "4":
        Patient.editPatientInfo()
      elif choose_patient == "5":
        print("Returning to Previous Menu\n")
      else:
        choose_patient = "x"
        print("Error! Please Try Again!\n")
  elif choice == "0":
    print("Closing Alberta Hospital(AH) Management System")
  else:
    choice = "x"
    print("Error! Please Try Again!\n")
