#!/usr/bin/env python
import sample.simple
import click

@click.command()
@click.option('--number', default=1, help='Number of greetings.')
def add_one(number):
    print(sample.simple.add_one(number))

if __name__ == '__main__':
    add_one()