from error_handler import ErrorHandler
from os import environ
import mysql.connector as mysqli

def paramsGenerator(data):
    print(data)
    if len(data.items())>0:
        if type(data) is dict:
            params = []
            values = []
            for key,val in data.items():
                params.append(key+" = %s")
                values.append(val)
            return " and ".join(params), values
        else:
            raise ErrorHandler("Params harus berupa dictionary")
    else:
        return "1", []
class dashboard:
    def __init__(self):
        self.client = mysqli.connect(
            host=environ.get("HOST",""),
            user=environ.get("USER",""),
            password=environ.get("PASSWORD",""),
            database=environ.get("DATABASE",""),
        )
        self.cursor = self.client.cursor()
    
    

    def getTemplates(self, data):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT * FROM templates where "+params, values)
            res = self.cursor.fetchone()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)
            raise ErrorHandler("Username gagal diambil, error pada server")
    
    def getData(self, data):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT * FROM data where "+params, values)
            res = self.cursor.fetchone()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)
            raise ErrorHandler("Username gagal diambil, error pada server")
    
    def getJoiner(self):
        try:
            self.cursor.execute("SELECT * FROM dashboard ")
            res = self.cursor.fetchall()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)
            raise ErrorHandler("Username gagal diambil, error pada server")

    # def getAllUser(self, data):
    #     try:
    #         params, values = paramsGenerator(data)
    #         self.cursor.execute("SELECT id_user, username, login_type FROM user where "+params, values)
    #         res = self.cursor.fetchall()
    #         self.result = {
    #             "data":res,
    #             "action":"select"
    #         }
    #         return self
    #     except Exception as e:
    #         print(e)
    #         raise ErrorHandler("Username gagal diambil, error pada server")
    
    # def postUser(self, data):
    #     try:
    #         col, param, val = (
    #             list(data.keys()), 
    #             ["%s" for x in range(len(data.items()))],
    #             list(data.values())
    #         )
    #         self.cursor.execute("INSERT INTO user ("+",".join(col)+") VALUES("+",".join(param)+")", val)
    #         self.client.commit()
    #         self.result = {
    #             "response":True,
    #             "action":"insert"
    #         }
    #         return  self
    #     except Exception as e:
    #         print(e)
    #         raise ErrorHandler("Username gagal diambil, error pada server")
    
    # def patchUser(self, data, where):
    #     try:
    #         params_up, val_up = paramsGenerator(data)
    #         params_wh, val_wh = paramsGenerator(where)
    #         val = val_up + val_wh
    #         self.cursor.execute("UPDATE user set "+params_up+" WHERE "+params_wh)
    #         self.client.commit()
    #         self.result = {
    #             "response":True,
    #             "action":"update"
    #         }
    #         return res
    #     except Exception as e:
    #         print(e)
    #         raise ErrorHandler("Username gagal diambil, error pada server")

    # def deleteUser(self, data):
    #     try:
    #         res = self.users.delete_one(data)
    #         return True
    #     except Exception as e:
    #         print(e)
    #         raise ErrorHandler("Username gagal diambil, error pada server")
    
    def getResult(self):
        # print(self.result)
        if self.result['action']=="select":
            column = self.cursor.description
            if type(self.result['data']) is tuple:
                row = self.result['data']
                data = {column[x][0]:row[x] for x in range(len(column))}
            if type(self.result['data']) is list:
                print(self.result['data'])
                data = [
                    {column[x][0]:row[x] for x in range(len(column))} for row in self.result['data']
                ]
            if self.result['data'] == None:
                data = None
            return data
        else:
            return False