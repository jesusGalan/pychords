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
            $scope.getTones = getTones;
            $scope.setNotes = setNotes;
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

        function getTones(grade) {
            if (grade == null) {
                return;
            }

            var reformatedGrade = grade.split(' ').join('_');

            scalesFactory.getTones(reformatedGrade).then(
                function(data) {
                    $scope.tones = [];
                    $scope.tonesNotesCorrespondency = [];

                    angular.forEach(data, function (value, key) {
                        $scope.tones.push(Object.keys(value)[0]);
                        $scope.tonesNotesCorrespondency.push(value);
                    });
                }
            );
        }

        function setNotes(tone) {
            angular.forEach($scope.tonesNotesCorrespondency, function (value, key) {
                if (tone == Object.keys(value)[0]) {
                    $scope.notes = value[tone];
                }
            });
        }
    }
})();
