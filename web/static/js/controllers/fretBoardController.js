(function() {
    'use strict';

    angular
        .module('app')
        .controller('fretBoardController', Controller);

    Controller.$inject = ['$scope', 'scalesFactory'];

    /* @ngInject */
    function Controller($scope, scalesFactory) {
        activate();

        function activate() {
            console.log('Activate fretBoardController view');

            $scope.getScaleGrades = getScaleGrades;
            $scope.scales = [];
            $scope.grades = [];

            scalesFactory.getAll().then(
                function(data) {
                    $scope.scales = data;
                }
            );
        }

        function getScaleGrades(scale) {
            if (scale.name == null) {
                return;
            }

            var reformatedScale = scale.name.split(' ').join('_');

            scalesFactory.getGrades(reformatedScale).then(
                function(data) {
                    $scope.grades = data;
                }
            );
        }
    }
})();
