/**
 * Playlists module
 * Methods
 *  - init OK
 *  - render OK
 *  - create OK
 *  - delete
 *  - activate
 * Loads
 *  - AJAX module
 */

var Playlists = (function () {
	var root = document.querySelector('.playlist');
	var divNode = document.createElement('div'); //ul
  divNode.className = 'playlist-inner';
	var createButton = root.querySelector('button');

	var playlists = [];
	var ajax = new Ajax();

	function render(){
		playlists.forEach(function(playlist){
			var p = _createPlaylistItem(playlist.name, playlist.id);
			divNode.appendChild(p);
		});
	}

	function create(name,id){
		var p = _createPlaylistItem(name,id);
		divtNode.appendChild(p);
	}

	function _createPlaylistItem(name, id) {
		var p = document.createElement('p');
		p.innerHTML = name;
		p.addEventListener('click', function(){
			console.log(p);
			// TODO: Render tracks
			Tracks.load(p);
		});
		return p;
	}

	return {
		init: function(){
			ajax.getPlaylists(function(res){
				playlists = res;
				render();
			});

			createButton.addEventListener('click',function(){
				var input = prompt('Enter playlist name');
				ajax.createPlaylists( input, function(rsp){
					console.log(rsp)
					create(input, rsp.id);
				});
			});
		},

		getPlaylists: function(){
			return playlists;
		}
	}
})();
