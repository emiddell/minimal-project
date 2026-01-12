#!/usr/bin/env python
import seminar_project.simple
import click

@click.command()
@click.option('--number', default=1, help='Number of greetings.')
def add_one(number):
    print(seminar_project.simple.add_one(number))

if __name__ == '__main__':
    add_one()
