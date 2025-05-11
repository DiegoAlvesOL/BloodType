import customtkinter
from customtkinter import CTkCheckBox, CTkButton
from BloodType import get_donation, receives_donation


# Função que trata a escolha do usuário e passa para as funções get_donation ou receives_donation
def handle_search():
    blood_type = blood_type_entry.get().strip().upper().replace(" ", "")
    name_user = user_name_entry.get().strip().title()

    if donate_var.get() and receive_var.get():
        result_text = "Please {}, select only one option at a time.".format(name_user)
    elif not donate_var.get() and not receive_var.get():
         result_text = "Please {}, select an option (donate or receive).".format(name_user)
    elif blood_type == "":
         result_text = "Please {}, enter your blood type.".format(name_user)
    else:
        if donate_var.get():
            result = receives_donation(blood_type)
            result_text = "Thank you {} for using Blood type.\nYour blood type is {}.\nThe blood types that can receive your blood are:\n{}:".format(name_user,blood_type,result)
        elif receive_var.get():
            result = get_donation(blood_type)
            result_text = "Thank you {} for using Blood type.\nYour blood type is {}. \nThe blood types you can receive are:\n{}".format(name_user, blood_type,result)
    display_result.configure(text=result_text)

mainWindown = customtkinter.CTk()
mainWindown.geometry("450x400")
mainWindown.title("Blood Type")
mainWindown.configure(fg_color="#051923")


# Welcome Frame
display_welcome_frame = customtkinter.CTkFrame(mainWindown, fg_color="#003554")
display_welcome_frame.grid(row=0, column=0, columnspan=3, pady=10,)

display_welcome = customtkinter.CTkLabel(display_welcome_frame,
                                         text="Welcome to the Blood Type Compatibility Checker",
                                         text_color="White",
                                         font=("Courier",14),
                                         wraplength=380,
                                         justify="center")
display_welcome.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

# frame para captura de dados, nome e tipo sanguineo
# depois passar o para o frama a configura fg_color="transparent"
entry_frame = customtkinter.CTkFrame(mainWindown)
entry_frame.grid(row=1,column=0,columnspan=3,pady=10, padx=10)

text_name = customtkinter.CTkLabel(entry_frame,
                                   text="Enter with your Name:",
                                   text_color="White",
                                   wraplength=200,
                                   justify="right")
text_name.grid(row=0,column=1,pady=5,padx=5)

user_name_entry = customtkinter.CTkEntry(entry_frame,
                                   placeholder_text="Name",
                                   width= 200,
                                   justify="center")
user_name_entry.grid(row=1,column=1,pady=5,padx=5)


text_blood = customtkinter.CTkLabel(entry_frame,
                                    text="Please, enter with your blood type: ",
                                    text_color="White",
                                    wraplength=300,
                                    justify="right")
text_blood.grid(row=0,column=3,pady=5,padx=5)
blood_type_entry = customtkinter.CTkEntry(entry_frame,
                                          placeholder_text="Blood type",
                                          width=200,
                                          justify="center")
blood_type_entry.grid(row=1,column=3,pady=5,padx=5)


# frame para colocar as opções se deseja doar ou receber sangue, as opções será através de checkbox
checkbox_frame = customtkinter.CTkFrame(mainWindown)
checkbox_frame.grid(row=2,column=0,columnspan=3,padx=10,pady=10)

# checkbox para receber doação de sangue.
donate_var = customtkinter.BooleanVar()
checkbox_get_donation = CTkCheckBox(checkbox_frame,
                                    text="Make a Donation",
                                    variable=donate_var,
                                    onvalue=True,
                                    offvalue=False)
checkbox_get_donation.grid(row=0,column=0,padx=10,pady=10)

#checkbox para doar sangue
receive_var = customtkinter.BooleanVar()
checkbox_receives_donation = CTkCheckBox(checkbox_frame,
                                         text="Receive a Donation",
                                         variable=receive_var,
                                         onvalue=True,
                                         offvalue=False)
checkbox_receives_donation.grid(row=0,column=3,padx=10,pady=10)

#  botão de pesquisa
check_button = CTkButton(mainWindown,
                         text="Search",
                         command=handle_search)
check_button.grid(row=3,columnspan=3,padx=10,pady=10)

# frame para exibir a mensagem.
display_result_frame = customtkinter.CTkFrame(mainWindown,
                                        fg_color="#003554")
display_result_frame.grid(row=4,column=0,columnspan=3,padx=10,pady=10)

display_result = customtkinter.CTkLabel(display_result_frame,
                                        text="",
                                        text_color="White",
                                        wraplength=500,
                                        justify="center")
display_result.grid(padx=10, pady=10)

mainWindown.mainloop()
