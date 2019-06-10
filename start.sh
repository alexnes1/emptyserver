#! /usr/bin/env bash

usage()
{
    echo "Empty server startup script"
    echo "Usage: ./start.sh [[[-h host ] [-p port ] [--production ] [-c ssl_cert -k ssl_key ]] | [--help ]]"
}

CERT=
KEY=
HOST=
PORT=
PRODUCTION=

if [ $# -eq 0 ]; then
    usage
    exit 0
fi

while [ "$1" != "" ]; do
    case $1 in
        -h | --host )           shift
                                HOST=$1
                                ;;
        -p | --port )           shift
                                PORT=$1
                                ;;
        -c | --cert )           shift
                                CERT=$1
                                ;;
        -k | --key )            shift
                                KEY=$1
                                ;;
        -pr | --production )    shift
                                PRODUCTION=1
                                ;;
        --help )                usage
                                exit
                                ;;
        * )                     usage
                                exit 1
    esac
    shift
done

if [ -z "$HOST" ] || [ -z "$PORT" ]
then
    usage
    echo "Missing parameter"
    exit 1
fi

HTTPS=
if [ ! -z "$CERT" ] || [ ! -z "$KEY" ]
then
    if [ ! -z "$CERT" ] && [ ! -z "$KEY" ]
    then
        HTTPS="--cert=$CERT --key=$KEY"
    else
        usage
        echo "Missing parameter"
        exit 1
    fi
fi

if [ -z "$PRODUCTION" ]
then
    export FLASK_ENV=development
fi

eval "python -m flask run --host=$HOST --port=$PORT $HTTPS"