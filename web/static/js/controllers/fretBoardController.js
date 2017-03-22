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
            $scope.getNotePositions = getNotePositions;

            scalesFactory.getAll().then(
                function(data) {
                    $scope.scales = data;
                }
            );
        }

        function getScaleGrades(scale) {
            $scope.grades = [];

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
            $scope.tones = [];
            $scope.tonesNotesCorrespondency = [];

            if (grade == null) {
                return;
            }

            var reformatedGrade = grade.split(' ').join('_');

            scalesFactory.getTones(reformatedGrade).then(
                function(data) {
                    angular.forEach(data, function (value, key) {
                        $scope.tones.push(Object.keys(value)[0]);
                        $scope.tonesNotesCorrespondency.push(value);
                    });
                }
            );
        }

        function setNotes(tone) {
            $scope.notes = [];

            angular.forEach($scope.tonesNotesCorrespondency, function (value, key) {
                if (tone == Object.keys(value)[0]) {
                    $scope.notes = value[tone];
                }
            });
        }

        function getNotePositions(note) {
            if (note == null) {
                return;
            }

            scalesFactory.getNotePositions(note).then(
                function(data) {
                    console.log(data);
                }
            );
        }
    }
})();
