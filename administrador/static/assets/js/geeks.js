function msjes_elimado(id) {
    const swalWithBootstrapButtons = Swal.mixin({
         customClass: {
           confirmButton: 'btn btn-success',
           cancelButton: 'btn btn-danger'
         },
         buttonsStyling: false
       })
       
       swalWithBootstrapButtons.fire({
         title: 'Estas Seguro?',
         text: "Despues de borrado no se puede revertir!",
         icon: 'warning',
         showCancelButton: true,
         confirmButtonText: 'Si, borrar!',
         cancelButtonText: 'No, cancelar!',
         reverseButtons: true
       }).then((result) => {
         if (result.isConfirmed) {
           swalWithBootstrapButtons.fire(
             'Borrado!',
             'El Registro ha sido Borrado!',
             'success'
           )
           window.location.href = "delete/"+id; 
         } else if (
           /* Read more about handling dismissals below */
           result.dismiss === Swal.DismissReason.cancel
         ) {
           swalWithBootstrapButtons.fire(
             'Cancelled',
             'El registro no fue borrado :)',
             'error'
           )
         }
       })
 }

 