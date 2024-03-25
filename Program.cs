//--------------------------------------------TAREA 1 ROBOTES--------------------------------------------
using System.Runtime.InteropServices;

internal class Program

{
    private static void Main(string[] args)
    {
        var rand = new Random();
        string[] Modelos= ["R2D2", "C3PO", "BBB"];
        Robot[] fabricaRobots = new Robot[0];
        bool controlOpciones=true;
        int opcion;


        while(controlOpciones){

            Console.WriteLine("0-Salir");
            Console.WriteLine("1- Agregar Robot");
            Console.WriteLine("2- Mostrar un robot a traves de su posicion");
            Console.WriteLine("3- Mostrar todos los robots");
            Console.WriteLine("4-Eliminar un robot");
            Console.WriteLine("5-Restablecer un robot");
            Console.WriteLine("----------------");
            Console.WriteLine("ingresa un opcion");
            opcion=Convert.ToInt32(Console.ReadLine());
            
            switch (opcion){
                case 0: Console.WriteLine("Fin Programma");
                        controlOpciones=false;
                        break;
                case 1: Console.WriteLine("Agregando Robot...");
                        fabricaRobots=crearRobots(fabricaRobots,rand,Modelos);
                        break;
                case 2: Console.WriteLine("Mostrando robot por posicion...");
                        mostratRobotPorPosicion(fabricaRobots);
                        break;
                case 3:Console.WriteLine("Mostrar Todo los robots...");
                        MostrarTodoRobots(fabricaRobots);
                        break;
                case 4:Console.WriteLine("Eliminar Robot...");
                        Console.WriteLine("Atencion:despues de eliminar se reordenaran las posiciones de los otros robots");
                        fabricaRobots=EliminarRobot(fabricaRobots);
                        break;
                case 5: Console.WriteLine("Restableciendo Robot...");
                        fabricaRobots=RestablecerRobots(fabricaRobots,rand);
                        break;
                default:Console.WriteLine("Opcion no valida");
                        Console.WriteLine("Ingresa una opcion nueva");
                        break;

            }

        }


    }
    //---------------------------------------------------------------------
    //El Struct del Robot(Cada robot tiene nombre,modelo,posicion)
    public struct Robot{
        public string nombre;
        public string modelo;
        public int posicion;
    }
    //--------------------Verificar--------------------------------------------------------------------------
    //----------------------------------------------------------------------
    //Funcion de Verificar si el nombre aleatoeio exite en la lista de robots.
    static string verificarNombres(Robot[] fabricaRobots,Random rand) {
       bool test;
       bool control=true;
       string nombreRobot=generalNombreAleatorio(rand);
       while(control){ /*Este while nos ayuda a generar un nombre aleatorio que no exista en la fabrica de robots*/
           test=false;
           foreach(Robot robot in fabricaRobots){
               if(robot.nombre==nombreRobot){
                   test=true;
                   break;
               }
           }
           if( test==false){
              control=false; 
           }
           else{
               nombreRobot=generalNombreAleatorio(rand);
           }
       }
       return nombreRobot;
    }
    //------------------CREAR--------------------------------------------------------------------------------------------
    //----------------------------------------------------------------------
    //Funcion de Crear un nuevo robot en la lista de robots.
    static Robot[] crearRobots(Robot[] fabricaRobots,Random rand,string[] Modelos) {
        Robot robotnuevo;
        string nombreRobot=verificarNombres(fabricaRobots,rand);
        robotnuevo.nombre=nombreRobot; //Asignamos el nombre aleatorio a la variable nombreRobot
        robotnuevo.modelo=generalModeloAleatorio(Modelos,rand); //Asignamos el modelo aleatorio a la variable modelo
        robotnuevo.posicion=fabricaRobots.Length; //Asignamos la posicion del robot en la lista de robots, utilizamos fabricaRobots.Count para saber la posicion del ultimo robot agregado
        fabricaRobots=subirTamano(fabricaRobots); //Subimos el tamanio de la lista de robots
        fabricaRobots[fabricaRobots.Length-1]=robotnuevo; //Agregamos el nuevo robot a la lista
        Console.WriteLine("El robot Creado Corectamente,Con los Siguientes Datos:");
        Console.WriteLine("Nombre: " + robotnuevo.nombre);
        Console.WriteLine("Modelo: "+robotnuevo.modelo);
        Console.WriteLine("Posicion: "+robotnuevo.posicion);
        return fabricaRobots;
    }
    //------------------------------------------------------------------------
    //Este Funcion Sirve Para subir El tamaño de la lista y Mover los Elementos Cuando queremos Agregar un nuevo Roboto a la Lista
    static Robot[] subirTamano(Robot[] fabricaRobots)
    {
        Robot[] fabricaRobots2 = new Robot[fabricaRobots.Length + 1];
        for(int i=0;i<fabricaRobots.Length;i++){
            fabricaRobots2[i]=fabricaRobots[i];
        }
        return fabricaRobots2;
    }
    //---------------------------Restablecer-----------------------------------------------------------------------------------
    //-----------------------------------------------------------------------
    //Funcion de restablecer la configuracion de un robot.
    static Robot[] RestablecerRobots(Robot[] fabricaRobots,Random rand) {
        int posicionRobot;
        do{ //Preguntamos por la posicion del robot que queremos restablecer
            Console.WriteLine("Ingresa la posicion del robot que deseas restablecer");
            posicionRobot=Convert.ToInt32(Console.ReadLine());
        }while(posicionRobot>=fabricaRobots.Length);
        Robot robotRestablecido=fabricaRobots[posicionRobot];
        robotRestablecido.nombre=verificarNombres(fabricaRobots,rand); //Asignamos un nuevo nombre aleatorio al robot
        fabricaRobots[posicionRobot]=robotRestablecido;
        Console.WriteLine("El nuevo nombre del robot es: "+robotRestablecido.nombre);
        return fabricaRobots;
    }
    //----------------------------Nombre y Modelos----------------------------------------------------------------------------
    //----------------------------------------------------------------------
    //Funcion de general un nombre aleatorio para un robot.
    static string generalNombreAleatorio(Random rand) //Funcion que nos ayuda a generar un nombre aleatorio
    {
            int randomNumber1 = rand.Next(0, 26); /*Este linaje genera un numero aleatorio entre 0 y 25,porque la funcion random acebta solo enteros*/
            int randomNumber2 = rand.Next(0, 26); /* En este parte de codigo aplicamos la formula para convertir el numero aleatorio a letra*/
            int numero1=rand.Next(0, 10);
            int numero2=rand.Next(0, 10);
            int numero3 = rand.Next(0, 10);
            char letraAleatoria1 = (char)('A' + randomNumber1);
            char letraAleatoria2 = (char)('A' + randomNumber2);
            string nombreRobot = $"{letraAleatoria1}{letraAleatoria2}{numero1}{numero2}{numero3}";
            return nombreRobot;
    }
    //---------------------------------------------------------------------
    //Funcion de general un Modelo Aleatario para un robot
    static string generalModeloAleatorio(string[] Modelos,Random rand){
        int randomNumber = rand.Next(0, Modelos.Length);
        string modelo = Modelos[randomNumber];
        return modelo;
    }
    //----------------------------------------Mostrar--------------------------------------------------------------------------------
    //--------------------------------------------------------------------
    //Funcion de mostrar un robot a traves de su posicion en la lista.
    static void mostratRobotPorPosicion(Robot[] fabricaRobots){
        int posicionMostrar;
        do{ //Preguntamos por la posicion del robot que queremos restablecer
            Console.WriteLine("Ingresa la posicion del robot que deseas restablecer");
            posicionMostrar=Convert.ToInt32(Console.ReadLine());
        }while(posicionMostrar>=fabricaRobots.Length);// Este while es para que no se salga de la lista de robots
        Console.WriteLine("El nombre del robot es: ");
        Console.WriteLine(fabricaRobots[posicionMostrar].nombre);
        Console.WriteLine("El modelo del robot es: ");
        Console.WriteLine(fabricaRobots[posicionMostrar].modelo);
        Console.WriteLine("La posicion del robot es: ");
        Console.WriteLine(fabricaRobots[posicionMostrar].posicion);
    }
    //----------------------------------------------------------------------
    //Funcion de Mostrar Todos los robots de la lista.
    static void MostrarTodoRobots(Robot[] fabricaRobots){
        foreach(Robot robot in fabricaRobots){
            Console.WriteLine("-----------------------");

            Console.WriteLine("Nombre: "+robot.nombre);

            Console.WriteLine("Modelo: "+robot.modelo);

            Console.WriteLine("Posicion:"+robot.posicion);
        }
    }
    //-------------------------------------------------------Eliminar-----------------------------------------------------------------
    //--------------------------------------------------------------------
    // Funcion de Eliminar un roboto de la lista.
    static Robot[] EliminarRobot(Robot[] fabricaRobots) {
        int posicionEliminar;
        do{
            Console.WriteLine("Ingresa la posicion del robot que deseas eliminar");
            posicionEliminar=Convert.ToInt32(Console.ReadLine());
        }while(posicionEliminar>=fabricaRobots.Length);
        fabricaRobots[posicionEliminar].nombre="";
        fabricaRobots[posicionEliminar].modelo="";
        //Aplicamos la funcion borrarNull para eliminar el robot nulo de la lista, y poner en su lugar el roboto siguiente
        fabricaRobots=borrarNull(fabricaRobots);
        Console.WriteLine("Robot eliminado correctamente");
        return fabricaRobots;
    }
    //------------------------------------------------------------------------
    //Este Funcion sirve para eliminar un robot nulo de la lista, y hacer un return de nueva lista sin robot nulo
    static Robot[] borrarNull(Robot[] fabricaRobots){
        Robot[] fabricaRobots2 = new Robot[CalcularCantidadRobots(fabricaRobots)];
        int indexfabricanteRobots2=0;// Este index nos ayudara a ubicar los robots en la nueva lista fabrianteRobots2
        for(int i=0;i<fabricaRobots.Length;i++){
            if(fabricaRobots[i].nombre!=""){
                fabricaRobots2[indexfabricanteRobots2]=fabricaRobots[i];
                indexfabricanteRobots2++;
            }
        }
        //Este codigo reasigna la posicion a los robots que no estan vacios, despues de borrar un roboto
        //Por Ejemplo tenemos 5 robots, y borrar el robot en la posicion 2, el robot en la posicion 3 se movera a la posicion 2
        for(int i=0;i<fabricaRobots2.Length;i++){
            fabricaRobots2[i].posicion=i;
        }
        return fabricaRobots2;
        
    }
    //------------------------------------------------------------------------
    // Este Funcion no sirve para Calcular Cuantos Robots hay en la fabrica que no son null, ya que solo borraria los null y no los que estan vacios
    static int CalcularCantidadRobots(Robot[] fabricaRobots){
        int comptador=0;
        for(int i=0;i<fabricaRobots.Length;i++){
            if (fabricaRobots[i].nombre!=""){
                comptador++;
            }
        }
        return comptador;
    }

}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//------------------------------------------------Tarea 2 Productos-----------------------------------------------------------------------



// internal class Program
// {
    

//     private static void Main(string[] args)
//     {

//         Producto[] productos=new Producto[20];
//         int opcion;
//         bool controlOpciones=true;


//         while(controlOpciones){

//             Console.WriteLine("0-Salir");
//             Console.WriteLine("1- Agregar Producto");
//             Console.WriteLine("2- Mostrar Productos");
//             Console.WriteLine("3- Editar un Producto");
//             Console.WriteLine("4- Eliminar un Producto");
//             Console.WriteLine("5- Mostrar Productos por categoria");
//             Console.WriteLine("----------------");
//             Console.WriteLine("ingresa un opcion");

//             opcion=Convert.ToInt32(Console.ReadLine());
//             switch (opcion){
//                 case 0: Console.WriteLine("Fin Programma");
//                         controlOpciones=false;
//                         break;
//                 case 1: Console.WriteLine("Agregando Producto...");
//                         productos=AgregarProducto(productos);
//                         break;
//                 case 2: Console.WriteLine("Mostrando Productos...");
//                         mostrarProductos(productos);
//                         break;
//                 case 3: Console.WriteLine("Editando un Producto...");
//                         productos=editarProducto(productos);
//                         break;
//                 case 4: Console.WriteLine("Eliminando un Producto...");
//                         productos=eliminarProducto(productos);
//                         break;
//                 case 5: Console.WriteLine("Mostrando Productos por categoria...");
//                         mostrarPorCategoria(productos);
//                         break;
//             }
//         }
//     }
//     public struct Producto{
//         public string nombre;
//         public string categoria;
//         public float precio;
//         public int cantidad;
//     }
//     //----------------------Agregar Producto--------------------------------------------------------------
//     static Producto[] AgregarProducto(Producto[] productos){
//         Producto productoNuevo;
//         bool control=false;

//         foreach(Producto producto in productos){
//             if(producto.nombre==null){
//                 control=true;
//                 break;
//             }
//         }

//         if(control==true){

//             Console.WriteLine("Ingresa el nombre del producto");
//             productoNuevo.nombre=Console.ReadLine();
//             Console.WriteLine("Ingresa la categoria del producto");
//             productoNuevo.categoria=Console.ReadLine();
//             Console.WriteLine("Ingresa el precio del Producto");
//             productoNuevo.precio=Convert.ToSingle(Console.ReadLine());
//             Console.WriteLine("Ingresa la cantidad del Producto");
//             productoNuevo.cantidad=Convert.ToInt32(Console.ReadLine());
//             for(int i=0;i<productos.Length;i++){
//                 if(productos[i].nombre==null){
//                     productos[i]=productoNuevo;
//                     break;
//                 }
//             }
            
//         }

//         else{
//            Console.WriteLine("No hay espacio para agregar mas productos");
//         }
//         return productos;
//     }
//     //-----------------------------------Eliminar un Producto-------------------------------------------------
//     static Producto[] eliminarProducto(Producto[] productos)
//     {
//         string nombreBorrar;
//         string categoriaBorrar;
//         bool control = true;
//         bool test = true;
//         while (control)
//         {
//             Console.WriteLine("Ingresa el nombre del producto que deseas eliminar");
//             nombreBorrar = Console.ReadLine();
//             Console.WriteLine("Ingresa la categoria del producto que deseas eliminar");
//             categoriaBorrar = Console.ReadLine();
//             foreach (Producto producto in productos)
//             {
//                 if (producto.nombre == nombreBorrar && producto.categoria == categoriaBorrar)
//                 {
//                     test = false;
                    
//                     break;
//                 }
//             }
//             if (test == false)
//             {
//                 for (int i = 0; i < productos.Length; i++)
//                 {
//                     if (productos[i].nombre == nombreBorrar && productos[i].categoria == categoriaBorrar)
//                     {
//                         productos[i].nombre = "";
//                         productos[i].categoria = "";
//                         productos[i].precio = 0;
//                         productos[i].cantidad = 0;

//                         break;
//                     }
//                 }
//                 control = false;
//             }
//             else
//             {
//                 Console.WriteLine("Este Producto Con ests datos no existe");
//             }
//         }
//         productos=borrarNull(productos);
//         return productos;
//     }
//     //Este Funcion sirve para eliminar un producto nulo de la lista, y hacer un return de nueva lista sin producto nulo
//     static Producto[] borrarNull(Producto[] productos){
//         Producto[] productos2 = new Producto[20];
//         int indexProductos=0;// Este index nos ayudara a ubicar los Productos en la nueva lista fabrianteProductos2

//         for(int i=0;i<productos.Length;i++){

//             if(productos[i].nombre!=null){
//                 productos2[indexProductos]=productos[i];
//                 indexProductos++;
//             }
//         }
//         return productos2;
        
//     }
//     //--------------------------------Editar un producto-----------------------------------------------------------
//     static Producto[] editarProducto(Producto[] productos)
//     {
//         string nombreEditar;
//         string categoriaEditar;
//         bool control = true;
//         int opcionEditar;

//         while (control){

//             Console.WriteLine("Ingresa el nombre del producto que deseas editar");
//             nombreEditar = Console.ReadLine();
//             Console.WriteLine("Ingresa la categoria del Producto que deseas editar");
//             categoriaEditar = Console.ReadLine();
//             for(int i=0;i<productos.Length;i++){

//                 if (productos[i].nombre == nombreEditar && productos[i].categoria == categoriaEditar)
//                 {
//                     do{

//                         Console.WriteLine("1. Editar Nombre.\n2. Editar Categoría.\n3. Editar Precio.\n4. Editar Cantidad");
//                         Console.WriteLine("Que deseas editar");
//                         opcionEditar=Convert.ToInt32(Console.ReadLine());

//                     }while(opcionEditar<1 || opcionEditar>4);

//                     switch (opcionEditar){
//                         case 1: productos[i].nombre=editarNombre(productos[i].nombre);
//                                 break;
//                         case 2: productos[i].categoria=editarCategoria(productos[i].categoria);
//                                 break;
//                         case 3: productos[i].precio=editarPrecio(productos[i].precio);
//                                 break;
//                         default: productos[i].cantidad=editarCantidad(productos[i].cantidad);
//                                  break;
//                     }
//                     control=false;
//                 }
//             }
//             if(control==true){
//                 Console.WriteLine("Este Producto Con ests datos no existe");
//             }
//             else{
//                 Console.WriteLine("Editado Correctamente");
//             }
            
//         }
//         return productos;
//     }
//     //-----------------------------Funciones de Editar------------------------------------
//     //----------Funcion de editar el Nombre--------------------------------
//     static string editarNombre(string nombreProducto){

//         Console.WriteLine("ingresa el nombre nuevo:");
//         string nombreNuevo=Console.ReadLine();
//         nombreProducto=nombreNuevo;
//         return nombreProducto;

//     }
//     //----------Funcion de editar la Categoría--------------------------------
//     static string editarCategoria(string categoria){
//         Console.WriteLine("ingresa la categoria nueva:");
//         string categoriaNueva=Console.ReadLine();
//         categoria=categoriaNueva;
//         return categoria;

//     }
//     //--------------Funcion de editar el Precio--------------------------------
//     static float editarPrecio(float precio){

//         Console.WriteLine("ingresa el precio nuevo:");
//         float precioNuevo=Convert.ToSingle(Console.ReadLine());
//         precio=precioNuevo;
//         return precio;

//     }
//     //--------------Funcion de editar la Cantidad--------------------------------
//     static int editarCantidad(int cantidad){

//         Console.WriteLine("ingresa la cantidad nueva:");
//         int cantidadNueva=Convert.ToInt32(Console.ReadLine());
//         cantidad=cantidadNueva;
//         return cantidad;

//     }
//     //-------------------------------------------------Mostrar Productos----------------------------------------
//     static void mostrarProductos(Producto[] productos){

//         foreach(Producto producto in productos){
//             if(producto.nombre!=null && producto.nombre!=""){
//                 Console.WriteLine("Los datos de este producto son:");
//                 Console.WriteLine("nombre: "+producto.nombre);
//                 Console.WriteLine("categoria: "+producto.categoria);
//                 Console.WriteLine("precio: "+producto.precio);
//                 Console.WriteLine("cantidad: "+producto.cantidad);
//                 Console.WriteLine("_____________________________");
//             }
//         }

//     }
//     //------------------------------------------------Mostrar Productos de Categoria------------------------------
//     static void mostrarPorCategoria(Producto[] productos){

//         bool control=true;

//         while(control){

//             Console.WriteLine("Ingresa la categoria del Producto");
//             string categoriaEliger=Console.ReadLine();
//             foreach(Producto producto in productos){
//                 if(producto.categoria==categoriaEliger){
//                     Console.WriteLine("Los datos de este Producto son:");
//                     Console.WriteLine("nombre: "+producto.nombre);
//                     Console.WriteLine("categoria: "+producto.categoria);
//                     Console.WriteLine("precio: "+producto.precio);
//                     Console.WriteLine("cantidad: "+producto.cantidad);
//                     Console.WriteLine("_____________________________");
//                     control=false;
//                 }
//             }
            
//             if(control==true){
//                 Console.WriteLine("No hay Productos de esta categoria");
//             }
//         }
        
//     }
// }


