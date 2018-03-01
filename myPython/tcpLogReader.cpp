///////////////////////////////////////////////////////////////////////
//
// src_ne/sys/cmn/tcpLogger/tcpLogReader.cpp
//
// Copyright (c) 2014 Infinera Corporation
//        All rights reserved.
//
///////////////////////////////////////////////////////////////////////

#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/time.h>

#include <Util/StdStreamUtil.h>

#include <ZSys.h>

void Usage( char const * cmdStr )
{
    std::cout << 
        "\n"
        "    Usage:\n"
        "\n"
        "    " << cmdStr << " <port> [<timeout=30>] [\"q\"]\n"
        "\n"
        "       - Starts a TCP log reader to output data from a TcpLogger application.\n"
        "\n"
        "       - The <port> parameter specifies the TCP port to accept connections.\n"
        "\n"
        "       - The optional <timeout> parameter specifies seconds to wait between\n"
        "         log messages before timing out the connection (default = 30).\n"
        "         Setting this value to 0 will prevent timeouts.\n"
        "         When timeouts are enabled, the TcpLogger application is expected\n"
        "         to output nulls occasionally when there are no log messages to output\n"
        "         to prevent the reader from timing out.\n"
        "\n"
        "       - The optional \"q\" parameter supports quiet mode,\n"
        "         which suppresses connect/disconnect messages.\n"
        << std::endl;
}

int main( int argc , char *argv[] )
{
    // If there is not 1, 2, or 3 arguments, just display usage.
    if (    ( argc < 2 )
        ||  ( argc > 4 ) )
    {
        Usage( argv[0] );
        return 1;
    }
    else
    {
        // Get port number argument.
        uint16 portNumArg;
        if ( !util::StringToNumber( portNumArg, argv[1] ) )
        {
            std::cout << argv[0] << " <port> parameter [" << argv[1] << "] must be a valid TCP port number" << std::endl;
            Usage( argv[0] );
            return 1;
        }
        int portNum = portNumArg;

        // Get timeout argument if present.
        uint32 timeout = 30;
        if ( argc > 2 )
        {
            if ( !util::StringToNumber( timeout, argv[2] ) )
            {
                std::cout << argv[0] << " parameter 2 <timeout> if present must be a positive integer or 0" << std::endl;
                Usage( argv[0] );
                return 1;
            }
        }

        // Get quiet argument if present.
        bool isQuiet = false;
        if ( argc > 3 )
        {
            if ( strcmp( argv[3], "q" ) == 0 )
            {
                isQuiet = true;
            }
            else
            {
                std::cout << argv[0] << " parameter 3 if present must be \"q\" - quiet mode" << std::endl;
                Usage( argv[0] );
                return 1;
            }
        }

        int sockfd;
        int sessionsockfd;
        struct sockaddr_in serv_addr;
        struct sockaddr_in cli_addr;
        socklen_t clilen = sizeof( cli_addr );

        sockfd = socket(AF_INET, SOCK_STREAM, 0);
        if ( sockfd < 0 ) 
        {
            std::cout << argv[0] << "- error opening socket" << std::endl;
            return 1;
        }

        memset((char *) &serv_addr, 0, sizeof(serv_addr));
        serv_addr.sin_family = AF_INET;
        serv_addr.sin_addr.s_addr = INADDR_ANY;
        serv_addr.sin_port = htons( portNum );

        if ( bind( sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr) ) < 0 )
        {
            std::cout << argv[0] << "- error binding socket" << std::endl;
            return 1;
        }

        if ( listen( sockfd, 1 ) < 0 )
        {
            std::cout << argv[0] << "- error on listen" << std::endl;
            return 1;
        }

        for (;;)
        {
            if ( !isQuiet )
            {
                std::cout << "Waiting for connection on port[" << portNum << "]" << std::endl;
            }

            sessionsockfd = accept( sockfd, (struct sockaddr *)&cli_addr, &clilen );
            if ( sessionsockfd < 0 ) 
            {
                std::cout << argv[0] << "- error on accept" << std::endl;
                return 1;
            }

            if ( !isQuiet )
            {
                std::cout << "Connection established" << std::endl; 
            }

            if ( timeout > 0 )
            {
                timeval tv = { timeout, 0 };
                if ( setsockopt( sessionsockfd, SOL_SOCKET, SO_RCVTIMEO, &tv, sizeof(tv) ) < 0 )
                {
                    std::cout << argv[0] << "- error on setsockopt SO_RCVTIMEO" << std::endl;
                    return 1;
                }
            }

            // Send null char to indicate that connection was complete.
            char msg[] = "";
            int n = write( sessionsockfd, msg, sizeof(msg) );
            if ( n == sizeof(msg) ) 
            {
                char buffer[ 4096 ];
                for (;;)
                {
                    // Read from socket with optional timeout.
                    errno = 0;
                    int n = read( sessionsockfd, &buffer[0], sizeof( buffer ) - 1 );
                    if ( n <= 0 )
                    {
                        if ( errno == EAGAIN )
                        {
                            std::cout << "---TIMEOUT---" << std::endl;
                        }

                        break; 
                    }

                    // Display text skipping over pings (nulls).
                    buffer[n] = 0;
                    for ( size_t i = 0; i < (size_t)n; ++i )
                    {
                        if ( buffer[i] != 0 )
                        {
                            std::cout << &buffer[i] << std::flush;

                            for ( ++i; i < (size_t)n; ++i )
                            {
                                if ( buffer[i] == 0 )
                                {
                                    break;
                                }
                            }
                        }
                    }
                }
            }

            if ( !isQuiet )
            {
                std::cout << "Connection lost" << std::endl;
            }
        }
    }

    return 0;
}

