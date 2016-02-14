describe('factory: EnrollmentsResource', function() {
  var enrollmentsResource;

  beforeEach(module('Pitchup'));

  beforeEach(inject(function(EnrollmentsResource) {
    enrollmentsResource = EnrollmentsResource;
  }));

  beforeEach(inject(function($httpBackend) {
    httpBackend = $httpBackend;
  }));

  afterEach(function() {
    httpBackend.verifyNoOutstandingExpectation();
    httpBackend.verifyNoOutstandingRequest();
  });

  describe('#postEnrollments', function() {
    it('returns a success message if a user has joined a team', function() {
      httpBackend
        .whenPOST("/teams/55/enrollments").respond(function() {
          return [201, { message: 'Successfully joined team!' }, {}];
        });
      enrollmentsResource.postEnrollments('2', 55)
        .then(function(data) {
          expect(data.message).toEqual('Successfully joined team!');
        });
        httpBackend.flush();
    });
  });
  describe('#postEnrollments error', function() {
    it('returns an error message if a user could not join a team', function() {
      httpBackend
        .whenPOST("/teams/55/enrollments").respond(400);
      enrollmentsResource.postEnrollments('2', 55)
        .then(function(data, status) {
          expect(status).toBe(400);
        });
      httpBackend.flush();
    });
  });
});
