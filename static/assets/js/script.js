    document.querySelectorAll('.toggle').forEach(item => {
        item.addEventListener('click', event => {
            const subList = item.nextElementSibling; // Get the next sibling (the sub_list)
            if (subList.style.display === 'block') {
                subList.style.display = 'none'; // Hide it if it's currently displayed
            } else {
                subList.style.display = 'block'; // Show it if it's currently hidden
            }
        });
    });

    document.getElementById("see-more-btn").addEventListener("click", function() {
        // Select all the hidden courses (those with the class 'more-courses')
        var hiddenCourses = document.querySelectorAll(".more-courses");
        
        // Loop through and reveal each hidden course
        hiddenCourses.forEach(function(course) {
            course.classList.remove("d-none");
        });
    
        // Hide the "See More" button after all courses are revealed
        this.style.display = "none";
    });


    function getCSRFToken() {
        // Get CSRF token from cookies
        var csrfToken = null;
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.startsWith('csrftoken=')) {
                csrfToken = cookie.substring('csrftoken='.length, cookie.length);
                break;
            }
        }
        return csrfToken;
    }

    $(document).ready(function(){
        // Like button click event
        $('.like-btn').on('click', function(){
            var courseId = $(this).data('course-id');  // Get the course ID from the button
            var likeCountElement = $('#like-count-' + courseId);  // Find the span for the like count
            var likeIconElement = $(this).find('i');  // Find the heart icon inside the like button

            $.ajax({
                url: '/courses/' + courseId + '/like/',  // URL to toggle like
                method: 'POST',
                headers: { 'X-CSRFToken': getCSRFToken() },  // Set CSRF token in request headers
                success: function(response) {
                    // Update the like count with the new value from the server
                    likeCountElement.text(response.likes_count);

                    // Toggle the heart icon based on the liked status
                    if (response.liked) {
                        likeIconElement.removeClass('ti-heart').addClass('ti-heart-broken');  // Change to filled heart
                    } else {
                        likeIconElement.removeClass('ti-heart-broken').addClass('ti-heart');  // Change back to empty heart
                    }
                },
                error: function(xhr, errmsg, err) {
                    console.log(xhr.status + ": " + xhr.responseText);  // Log any errors
                }
            });
        });
    });



    // signup
    $(document).ready(function() {
        $('#id_phone_code').select2({
            placeholder: "Select your country code",
            allowClear: true
        });
    });