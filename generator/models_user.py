from lib import write, read, get

class User:
    file_name = 'user.json'
    def __init__(self, pk = None):
        self.pk = pk
        self.username = ''
        if pk:
            user = get(self.pk, self.file_name)
            if user:
                self.username = user['username']
        try:
            self.lista_users = read(self.file_name)
        except FileNotFoundError:
            self.lista_users = []

    def save(self):
        '''Salva nome do usuario'''
        self.generate_pk()    
        dict_user = {} 
        dict_user['pk'] = self.pk
        dict_user['username'] = self.username
        self.lista_users.append(dict_user)   
        write(self.lista_users, self.file_name)
        print(f'User pk {self.pk} adicionado')

    def generate_pk(self):
        '''Define o numero pk de cada usuario'''
        lista_pk = []
        if not self.lista_users:
            self.pk = 1
            return
        for user in self.lista_users:
            lista_pk.append(user["pk"])   
        self.pk = max(lista_pk) + 1
            
    def update(self):
        for user in self.lista_users:
            if self.pk == user["pk"]:
                user['username'] = self.username
        write(self.lista_users, self.file_name)
        
    def delete(self):
        new_users = []
        for user in self.lista_users:
            if self.pk != user["pk"]:
                new_users.append(user)
        write(new_users, self.file_name)
