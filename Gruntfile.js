module.exports = function(grunt) {
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		sass: {
			dist: {
				files: [{
	        expand: true,
	        cwd: 'app/static/sass',
	        src: ['*.scss'],
	        dest: 'app/static/css',
	        ext: '.css'
	      }]
			}
		},
		watch: {
			css: {
				files: 'app/static/sass/*.scss',
				tasks: ['sass']
			}
		}
	});
	grunt.loadNpmTasks('grunt-contrib-sass');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.registerTask('default',['watch']);
	grunt.registerTask('prod',['sass']);
}
