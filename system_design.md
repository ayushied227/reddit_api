

Functional Requirements - 
Should be able to signup/login/logout
Should be able to post questions, and be able to add tags.
Should be able to add answers.
Should be able to add comments to both questions and answers.
Users should get a notification when their question is answered or a comment is added to their post (question or answer)
OP should be able to mark answers as “This worked for me”
Users should be able to upvote or downvote posts.
As a user, you should be able to see all your posts, access your profile.
Chat system.


Signup etc is trivial.

Data and Databases
Lets consider the data that we would want to store.
For users - 
Name
Email
Username
Password
Bio
Reputation (this is just the sum of all the upvotes the user has ever received)
Location

We would like all the users to have these fields, plus user data is generally not required all at once, and frequently. So using an RDBMS like postgres makes sense.

It makes sense to me, to have separate models for questions, answers, and comments.
Why? Better organization this way. Plus, a bigger model would take that much more time to query, so it is better to split data when there is such a clear distinction.

Now these three have optional parameters such as tags, upvote_count, media, bookmark_count etc, and additional fields might be added later. So using a nosql db (mongodb maybe) makes sense. 

Since we are not expecting a lot of pictures, s3 is okay as a storage service.



A typical question object might look like
{
	Question: text,
	Description: rich text,
	Tags: {
	Tag_object_id: tag_object_name
}
Media: textfield (url)
Upvote_count: int
}

A typical answer object might look like
{
	Answer: rich text,
	Media: text,
	Upvote_count: int,
	Question: question_id
}

A typical comment might look like
{
	Comment: textfield.
	Parent: parent_id
}



The APIs - 
Create_new_post 
		This can take title*, description*, tags*
get_post(post_id) - this will get you the post.
Additionally, all the answers, and the respective comments for all answers.
Update_post
Post_id, updated_title, updated_text
Delete_post(post_id)
Update_answer(answer_id)
Delete_answer(answer_id)

Is it a good design to get all answers and comments with the post? This increases the load time, surely. 
An alternative is to get the text, and push all the answer queries to message queues, from where they will be delivered as soon as they are loaded.

upvote(object_id)
Get the object, increase its like_count by 1.
downvote(object_id)
Get the object, increase
add_tag(question_id)
remove_tag(question_id)
