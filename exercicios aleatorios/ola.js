livro = {

    'titulo':'Harry Potter',
    'autor':'Lucas Speranzini',
    'Páginas lidas':50,
    'Leu':false,
    'descricao': function(){

        console.log(`O livro ${this.titulo} do ${this.autor} é uma obra clássica!!`)
    }
}

console.log(livro.descricao())
    
