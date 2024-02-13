
# SUBST Server


import socket
import string
def encrypt(text,key):
    all_letters=string.ascii_letters
    dict1={}
    for i in range(len(all_letters)):
        dict1[all_letters[i]]=all_letters[(i+key)%len(all_letters)]
    encrypted_text=[]
    for char in text:
        if char in all_letters:
            temp=dict1[char]
            encrypted_text.append(temp)
        else:
            temp=char
            encrypted_text.append(temp)
    return "".join(encrypted_text),dict1
def start_server():
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='127.0.0.1'
    port=12344
    server_socket.bind((host,port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    while True:
        client_socket,addr=server_socket.accept()
        print('Got connection from',addr)
        data=client_socket.recv(1024).decode('utf-8')
        print(f"Received data from the client:{data}")
        key=4
        encrypted_data,substitution_dict=encrypt(data,key)
        print(f"Encrypted data:{encrypted_data}")
        print("Substitution steps:")
        for original,substituted in substitution_dict.items():
            print(f"{original}->{substituted}")
        client_socket.send(encrypted_data.encode('utf-8'))
        client_socket.close()
if __name__=="__main__":
    start_server()


#OUTPUT

#Server listening on 127.0.0.1:12344
#Got connection from ('127.0.0.1', 58402)
#Received data from the client:Hello
#Encrypted data:Lipps
#Substitution steps:
#a->e
#b->f
#c->g
#d->h
#e->i
#f->j
#g->k
#h->l
#i->m
#j->n
#k->o
#l->p
#m->q
#n->r
#o->s
#p->t
#q->u
#r->v
#s->w
#t->x
#u->y
#v->z
#w->A
#x->B
#y->C
#z->D
#A->E
#B->F
#C->G
#D->H
#E->I
#F->J
#G->K
#H->L
#I->M
#J->N
#K->O
#L->P
#M->Q
#N->R
#O->S
#P->T
#Q->U
#R->V
#S->W
#T->X
#U->Y
#V->Z
#W->a
#X->b
#Y->c
#Z->d
