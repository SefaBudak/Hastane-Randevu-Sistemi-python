from tkinter import*
from tkinter import ttk
import random
import time
import datetime
import tkinter.messagebox

    #create class hospital 
class Hospital:
    #constructor
    def __init__(self,root):
        self.root = root
        self.root.title("Hastane Randevu Sistemi")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')


        cmbNameTablets = StringVar()
        Ref = StringVar()
        Dose = StringVar()
        NumberTablets = StringVar()
        Lot = StringVar()
        IssueDate = StringVar()
        ExpDate = StringVar()
        DailyDose = StringVar()
        PossibleSideEffects = StringVar()
        FurtherInformation = StringVar()
        StorageAdvice = StringVar()
        DrivingUsingMachines = StringVar()
        HowtoUseMedication = StringVar()
        PatientID = StringVar()
        PatientNHSNo = StringVar()
        PatientName = StringVar()
        DateofBirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()
        #==============================Funtion declaration============================================
        def iExit():
            iExit=tkinter.messagebox.askyesno("Hastane Randevu Sistemi","Çıkmayı Onaylıyor musunuz?")
            if iExit >0:
                root.destroy()
                return
        def iPrescription():

            self.txtPrescription.insert(END,'Hastalık:\t\t\t' + cmbNameTablets.get()+ "\n")
            self.txtPrescription.insert(END,'Sıra Numarası:\t\t\t' + Ref.get()+ "\n")
            self.txtPrescription.insert(END,'Kimlik Numarası:\t\t\t' + Dose.get()+ "\n")
            self.txtPrescription.insert(END,'Hasta Soyadı:\t\t\t' + Lot.get()+ "\n")
            self.txtPrescription.insert(END,'Randevu Tarihi:\t\t\t' + IssueDate.get()+ "\n")
            self.txtPrescription.insert(END,'Muayne Tarihi:\t\t\t' + ExpDate.get()+ "\n")
            self.txtPrescription.insert(END,'Hasta Şikayeti:\t\t\t' + DailyDose.get()+ "\n")
            self.txtPrescription.insert(END,'Belirtiler:\t\t\t' + PossibleSideEffects.get()+ "\n")
            self.txtPrescription.insert(END,'Tanı:\t\t\t' + FurtherInformation.get()+ "\n")
            self.txtPrescription.insert(END,'İlaç:\t\t\t' + StorageAdvice.get()+ "\n")
            self.txtPrescription.insert(END,'İlaç Yan Etkileri:\t\t\t' + DrivingUsingMachines.get()+ "\n")
            self.txtPrescription.insert(END,'Günlük Doz:\t\t\t' + PatientID.get()+ "\n")
            self.txtPrescription.insert(END,'Rapor Durumu:\t\t\t' + PatientNHSNo.get()+ "\n")
            self.txtPrescription.insert(END,'İzinli Gün Sayısı:\t\t\t' + PatientName.get()+ "\n")
            self.txtPrescription.insert(END,'Ev Adersi:\t\t\t' + DateofBirth.get()+ "\n")
            self.txtPrescription.insert(END,'Doktor Yorumu:\t\t\t' + PatientAddress.get()+ "\n")
            return

        def iReciept():
            

            self.txtFrameDetail.insert(END, cmbNameTablets.get()+"\t\t" + Ref.get()+"\t"+Dose.get()+"\t"+ NumberTablets.get()+"\t"+Lot.get()+"\t"+IssueDate.get()+"\t"+ExpDate.get()+"\t"+DailyDose.get()+"\t\t"+ StorageAdvice.get()+"\t"+ PatientNHSNo.get() + "\t\t" + PatientName.get()+ "\t" + PatientAddress.get()+ "\n")
            return 

        def iDelete():

            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("") 
            PatientID.set("")
            PatientNHSNo.set("") 
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)
            return 

        def iReset():
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("") 
            PatientID.set("")
            PatientNHSNo.set("") 
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            #self.txtFrameDetail.delete("1.0",END)
            return    










       #==================Main frame====================================================
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame (MainFrame,bd=20, width=1350,padx=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle =Label(TitleFrame,font=('arial',40,'bold'),text="Hastane Randevu Sistemi",padx=2)
        self.lblTitle.grid()
        #====================MainFrame ===============
        FrameDetail=Frame(MainFrame,bd=20,width=1350,height=100,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame=Frame(MainFrame,bd=20,width=1350,height=100,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=20,width=1350,height=400,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT=LabelFrame(DataFrame,bd=10,width=800,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'),text="Hasta Bilgileri:")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT=LabelFrame(DataFrame,bd=10,width=450,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'),text="Reçete")
        DataFrameRIGHT.pack(side=RIGHT)
        #========================Data Frame Left=================================================
        self.lblNameTablet =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Yaygın Hastalıklar",padx=2,pady=2)
        self.lblNameTablet.grid(row =0, column=0, sticky=W)

        self.cboNameTablet=ttk.Combobox(DataFrameLEFT,textvariable=cmbNameTablets, state ='readonly',font=('arial',12,'bold'),width=20)
        self.cboNameTablet['value']=('','İnfluenza ','Diyabet','Hipertansiyon ','Kanser','Felç ','Menenjit','Astım','Zatürre ')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0,column=1)

        self.lblFurtherInfo =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Tanı: ",padx=2,pady=2)
        self.lblFurtherInfo.grid(row =0, column=2, sticky=W)
        self.txtFurtherInfo =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=FurtherInformation,width=25)
        self.txtFurtherInfo.grid(row =0, column=3)

        self.lblRef =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Sıra Numarası:",padx=2,pady=2)
        self.lblRef.grid(row =1, column=0, sticky=W)
        self.txtRef =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Ref,width=25)
        self.txtRef.grid(row =1, column=1)

        self.lblStorage =Label(DataFrameLEFT,font=('arial',12,'bold'),text="İlaç:",padx=2,pady=2)
        self.lblStorage.grid(row =1, column=2, sticky=W)
        self.txtStorage =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=StorageAdvice,width=25)
        self.txtStorage.grid(row =1, column=3)

        self.lblDose =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Kimlik Numarası:",padx=2,pady=2)
        self.lblDose.grid(row =2, column=0, sticky=W)
        self.txtDose=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Dose, width=25)
        self.txtDose.grid(row =2, column=1)

        self.lblUseMachine =Label(DataFrameLEFT,font=('arial',12,'bold'),text="İlaç Yan Etkileri:",padx=2,pady=2)
        self.lblUseMachine .grid(row =2, column=2, sticky=W)
        self.txtUseMachine =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=DrivingUsingMachines, width=25)
        self.txtUseMachine .grid(row =2, column=3)
        
        self.lblNoOfTablets =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Hasta Adı:",padx=2,pady=2)
        self.lblNoOfTablets .grid(row =3, column=0, sticky=W)
        self.txtNoOfTablets =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=NumberTablets, width=25)
        self.txtNoOfTablets .grid(row =3, column=1)

        self.lblUseMedication =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Kullanım Şekli:",padx=2,pady=2)
        self.lblUseMedication .grid(row =3, column=2, sticky=W)
        self.txtUseMedication =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=HowtoUseMedication, width=25)
        self.txtUseMedication.grid(row =3, column=3)
        
        self.lblLot =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Hasta Soyadı:",padx=2,pady=2)
        self.lblLot .grid(row =4, column=0, sticky=W)
        self.txtLot =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Lot, width=25)
        self.txtLot.grid(row =4, column=1)

        self.lblPatientID =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Günlük Doz:",padx=2,pady=2)
        self.lblPatientID .grid(row =4, column=2, sticky=W)
        self.txtPatientID =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PatientID, width=25)
        self.txtPatientID.grid(row =4, column=3)

        self.lblIssueDate =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Randevu Tarihi:",padx=2,pady=2)
        self.lblIssueDate .grid(row =5, column=0, sticky=W)
        self.txtIssueDate =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=IssueDate, width=25)
        self.txtIssueDate.grid(row =5, column=1)
        
        self.lblNHSNumber =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Rapor Durumu:",padx=2,pady=2)
        self.lblNHSNumber.grid(row =5, column=2, sticky=W)
        self.txtNHSNumber =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= PatientNHSNo, width=25)
        self.txtNHSNumber.grid(row =5, column=3)
        
        self.lblExpDate =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Muayne Tarihi:",padx=2,pady=2)
        self.lblExpDate.grid(row =6, column=0, sticky=W)
        self.txtExpDate =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= ExpDate, width=25)
        self.txtExpDate.grid(row =6, column=1)

        self.lblPatientName =Label(DataFrameLEFT,font=('arial',12,'bold'),text="İzinili Gün Sayısı:",padx=2,pady=2)
        self.lblPatientName.grid(row =6, column=2, sticky=W)
        self.txtPatientName =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= PatientName, width=25)
        self.txtPatientName.grid(row =6, column=3)

        self.lblDailyDose =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Hasta Şikayeti:",padx=2,pady=2)
        self.lblDailyDose.grid(row =7, column=0, sticky=W)
        self.txtDailyDose =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= DailyDose, width=25)
        self.txtDailyDose.grid(row =7, column=1)

        self.lblDateofBirth=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Ev Adresi:",padx=2,pady=2)
        self.lblDateofBirth.grid(row =7, column=2, sticky=W)
        self.txtDateofBirth =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= DateofBirth, width=25)
        self.txtDateofBirth.grid(row =7, column=3)

        self.lblSideEffects=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Belirtiler:",padx=2,pady=2)
        self.lblSideEffects.grid(row =8, column=0, sticky=W)
        self.txtSideEffects =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= PossibleSideEffects, width=25)
        self.txtSideEffects.grid(row =8, column=1)

        self.lblPatientAddress=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Doktor Yorumu:",padx=2,pady=2)
        self.lblPatientAddress.grid(row =8, column=2, sticky=W)
        self.txtPatientAddress =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= PatientAddress, width=25)
        self.txtPatientAddress.grid(row =8, column=3)
        
        #=======================DataFrameRight=============================================
        
        self.txtPrescription=Text(DataFrameRIGHT,font=('arial',12,'bold'),width=43,height=11,padx=2,pady=6)
        self.txtPrescription.grid(row =0, column=0)


        #=======================ButtonFrame=============================================
        self.btnPrescription=Button(ButtonFrame, text='Reçete',font=('arial',12,'bold'),width=24,bd=4,bg="light blue",command =iPrescription)
        self.btnPrescription.grid(row=0,column=0) 

        self.btnReciept=Button(ButtonFrame, text='Fiş',font=('arial',12,'bold'),width=24,bd=4,bg="light blue",command= iReciept)
        self.btnReciept.grid(row=0,column=1) 
       
        self.btnDelete=Button(ButtonFrame, text='Sil',font=('arial',12,'bold'),width=24,bd=4,bg="light blue", command= iDelete)
        self.btnDelete.grid(row=0,column=2) 
        
        self.btnReset=Button(ButtonFrame, text='Yenile',font=('arial',12,'bold'),width=24,bd=4,bg="light blue",command= iReset)
        self.btnReset.grid(row=0,column=3) 

        self.btnExit=Button(ButtonFrame, text='Çıkış',font=('arial',12,'bold'),width=24,bd=4,bg="light blue",command=iExit)
        self.btnExit.grid(row=0,column=4) 
       
       
       
       
       
       
       
        #=======================FrameDetail=============================================
        
        self.lblLabel =Label(FrameDetail,font=('arial',10,'bold'),text="Hastalık\t Sıra Numarası.\t Kimlik Numarası\t Hasta Adı\t Lot \t Hasta Soyadı\t Randevu Tarihi\t Muayne Tarihi\t Hasta Şikayeti\t Belirtiler\t Tanı\t İlaç\t İlaç Yan Etkileri",pady=8)
        self.lblLabel.grid(row=0,column=0)

        self.txtFrameDetail=Text(FrameDetail,font=('arial',12,'bold'),width=141,height=7,padx=2,pady=4)
        self.txtFrameDetail.grid(row =1, column=0)
         





        



if __name__ == '__main__':
  root=Tk()
  application=Hospital(root)
  root.mainloop()




        

