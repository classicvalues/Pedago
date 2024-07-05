# pedago/cli.py

import click
from pedago.course.course_manager_wrapper import CourseManagerWrapper

course_manager = CourseManagerWrapper()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('title')
@click.argument('description')
@click.argument('start_date')
@click.argument('end_date')
@click.argument('teacher_id')
def create_course(title, description, start_date, end_date, teacher_id):
    course_id = course_manager.createCourse(title, description, start_date, end_date, teacher_id)
    click.echo(f'Course created with ID: {course_id}')

if __name__ == '__main__':
    cli()
