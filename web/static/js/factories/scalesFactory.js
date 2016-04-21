(function() {
    'use strict';

    angular
        .module('app')
        .factory('scalesFactory', factory);

    factory.$inject = ['$http'];

    /* @ngInject */
    function factory($http) {
        var service = {
            getAll: getAll,
            getGrades: getGrades,
            getTones: getTones
        };

        return service;

        function getAll() {
            return $http.get('/api/scale/')
                .then(getAllComplete)
                .catch(getAllFail);

            function getAllComplete(response) {
                return response.data;
            }

            function getAllFail(error) {
                console.error('XHR Failed for scalesFactory.getAll.', error.data);
            }
        }

        function getGrades(scale) {
            return $http({
                url: '/api/grades/',
                method: 'GET',
                params: {scale: scale},
            })
                .then(getGradesComplete)
                .catch(getGradesFail);

            function getGradesComplete(response) {
                return response.data;
            }

            function getGradesFail(error) {
                console.error('XHR Failed for scalesFactory.getGrades.', error.data);
            }
        }

        function getTones(grade) {
            return $http({
                url: '/api/tones/',
                method: 'GET',
                params: {grade: grade}
            })
                .then(getTonesComplete)
                .catch(getTonesFail);

            function getTonesComplete(response) {
                return response.data;
            }

            function getTonesFail(error) {
                console.error('XHR Failed for scalesFactory.getTones', error.data);
            }
        }
    }
})();
