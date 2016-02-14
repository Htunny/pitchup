pitchup.factory('EnrollmentsResource', ['$http', '$q', function($http, $q) {
  var enrollmentsResource = {};

  enrollmentsResource.postEnrollments = function(number_players, id) {
    var deferred = $q.defer();
    $http.post('/teams/' + id + '/enrollments', {number_players: number_players})
      .success(function (data, status) {
        if(status === 201){
          deferred.resolve(data);
        }
      })
      .error(function(data) {
        deferred.reject();
      });
    return deferred.promise;
  };

  return enrollmentsResource;
}]);
