(function($) {
	$(document).ready(function() {
		selectNoCobranza = $('#id_id_motivo_no_cobranza');
		selectNoPedido = $('#id_id_motivo_no_pedido');
		selectNoVisita = $('#id_id_motivo_no_visita');

		selectNoVisita.on('change', function() {
			if (this.value != "") {
				selectNoCobranza.val("").prop('disabled', 'disabled');
				selectNoPedido.val("").prop('disabled', 'disabled');
			} else {
				selectNoCobranza.prop('disabled', '');
				selectNoPedido.prop('disabled', '');
			}
		})

		function disableVisita(elem,other){
			if (elem.value != "") {
				selectNoVisita.val("").prop('disabled', 'disabled');
			} else {
				if (selectNoPedido.val() == '') {
					selectNoVisita.prop('disabled', '');
				}
			}
		}
		
		selectNoCobranza.on('change', function() {
			disableVisita(this,selectNoPedido);
		})

		selectNoPedido.on('change', function() {
			disableVisita(this,selectNoCobranza);
		})
		
		
	})
})(django.jQuery);