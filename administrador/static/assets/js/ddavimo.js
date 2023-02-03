// Token de Seguridad 
function getCookie(c_name) {
    if(document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if(c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if(c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}
// Sweet Alert 
// Mensajes de Error 
function msjes_error(m) {
    Swal.fire({
        icon: 'error',
        title: '!ERROR¡',
        text: '! ' + m + ' ¡',
    })
}
// Mensajes de Agregado 
function msjes_agregado() {
    Swal.fire({        
        icon: 'success',
        title: 'Su Registro ha sido salvado',
        showConfirmButton: true ,       
    }).then((result) => {
    if (result.isConfirmed) {
        location.reload();
    }
    }) 
}
// Mensajes de eliminados 

function msjes_elimado(codCafe) {
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
          feliminar(codCafe); 
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

//  Funcion Agregar registros a tablas 
function fagregar(event) {   
    event.preventDefault();     
    var ldata = $("#Cafe_form").serialize();
    $.ajax({
        type: "POST",
        url: "/agregar/",
        data: ldata,
        headers : {
            "X-CSRFToken": getCookie("csrftoken")
        },
        success: function (response) {
            console.log(response);
            msjes_agregado();       
        },
        error: function (xhr, ajaxOptions, thrownError, response) {
            if (xhr.status == 400) {
            var datos = JSON.parse(xhr.responseText);
            m = datos.error.codCafe;
            msjes_error(m);
            } else {
            alert('otro error')
            }
        }
    })
}

// Funcion de Eliminar registros 
function feliminar(codCafe) {     
    $.ajax({
        type: "POST",
        url: "/eliminar/",
        data: {
            "codCafe": codCafe
        },
        headers : {
            "X-CSRFToken": getCookie("csrftoken")
        },
        success: function () {         
          
            let timerInterval
                Swal.fire({
                title: 'Registro Borrado',
                html: 'I will close in <b></b> milliseconds.',
                timer: 1000,
                timerProgressBar: true,
                didOpen: () => {
                    Swal.showLoading()
                    const b = Swal.getHtmlContainer().querySelector('b')
                    timerInterval = setInterval(() => {
                    b.textContent = Swal.getTimerLeft()
                    }, 100)
                },
                willClose: () => {
                    clearInterval(timerInterval)
                }
                }).then((result) => {
                /* Read more about handling dismissals below */
                location.reload(); 
                if (result.dismiss === Swal.DismissReason.timer) {
                    console.log('Borrando registro')
                }
                })
           
        },
      
    })

}



