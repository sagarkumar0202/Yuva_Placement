import mysql.connector
import streamlit as st

# Establish a connection to MySQL Server

mydb = mysql.connector.connect(
    host='sql12.freesqldatabase.com',
    user='sql12782800',
    password='Sagar@0407',
    database="sql12782800"


)

mycursor=mydb.cursor()
print("Connection Established")

# Create Streamlit App

def main():
    st.header("Register Yourself With Software Power Hub");

    # Display Options for CRUD Operations
    option=st.sidebar.selectbox("Select an Operation",("Create","Read","Update","Delete"))
    
    
    # Perform Selected CRUD Operations
    if option=="Create":
        st.subheader("Create a Record")
        name=st.text_input("Enter Your Name")
        mobile=st.text_input("Enter Your Mobile Number")
        email=st.text_input("Enter Your Email")
        Address=st.text_input("Enter Your Addres")

    
        if st.button("Create"):
            sql= "insert into reg(name,mobile,email,Address) values(%s,%s,%s,%s)"
            val= (name,mobile,email,Address)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Created Successfully!!!")



    elif option=="Read":
        st.subheader("Read Records")
        mycursor.execute("select * from reg")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)



    elif option=="Update":
        st.subheader("Update a Record")
        id=st.number_input("Enter ID",min_value=1)
        name=st.text_input("Enter New Name")
        mobile=st.text_input("Enter Your Mobile Number")
        email=st.text_input("Enter Your Email")
        Address=st.text_input("Enter Your Addres")
        if st.button("Update"):
            sql="update reg set name=%s,mobile=%s,email= %s,Address= %s where id =%s"
            val=(name,mobile,email,Address,id)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")




    elif option=="Delete":
        st.subheader("Delete a Record")
        id=st.number_input("Enter ID",min_value=1)
        if st.button("Delete"):
            sql="delete from reg where id =%s"
            val=(id,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")


if __name__ == "__main__":  
    main()