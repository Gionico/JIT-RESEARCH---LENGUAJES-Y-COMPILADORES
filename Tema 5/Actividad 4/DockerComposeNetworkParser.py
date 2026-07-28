# Generated from DockerComposeNetwork.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,3,1,31,8,1,1,1,1,1,3,1,35,8,1,1,2,1,2,1,2,1,2,4,2,41,8,
        2,11,2,12,2,42,1,3,1,3,1,3,1,3,1,3,1,3,4,3,51,8,3,11,3,12,3,52,1,
        4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,4,5,64,8,5,11,5,12,5,65,1,6,1,
        6,1,6,1,6,1,6,1,6,4,6,74,8,6,11,6,12,6,75,1,7,1,7,1,7,1,7,1,7,1,
        7,4,7,84,8,7,11,7,12,7,85,1,7,1,7,1,7,1,7,3,7,92,8,7,1,8,1,8,1,8,
        1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,1,2,0,3,6,9,9,101,0,21,
        1,0,0,0,2,34,1,0,0,0,4,36,1,0,0,0,6,44,1,0,0,0,8,54,1,0,0,0,10,59,
        1,0,0,0,12,67,1,0,0,0,14,91,1,0,0,0,16,93,1,0,0,0,18,20,3,2,1,0,
        19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,
        0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,35,3,4,2,0,27,
        35,3,10,5,0,28,35,3,16,8,0,29,31,5,8,0,0,30,29,1,0,0,0,30,31,1,0,
        0,0,31,32,1,0,0,0,32,35,3,16,8,0,33,35,5,12,0,0,34,26,1,0,0,0,34,
        27,1,0,0,0,34,28,1,0,0,0,34,30,1,0,0,0,34,33,1,0,0,0,35,3,1,0,0,
        0,36,37,5,1,0,0,37,40,5,11,0,0,38,39,5,8,0,0,39,41,3,6,3,0,40,38,
        1,0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,5,1,0,0,0,44,
        45,5,9,0,0,45,46,5,2,0,0,46,50,5,11,0,0,47,48,5,8,0,0,48,49,5,8,
        0,0,49,51,3,8,4,0,50,47,1,0,0,0,51,52,1,0,0,0,52,50,1,0,0,0,52,53,
        1,0,0,0,53,7,1,0,0,0,54,55,7,0,0,0,55,56,5,2,0,0,56,57,5,10,0,0,
        57,58,5,11,0,0,58,9,1,0,0,0,59,60,5,7,0,0,60,63,5,11,0,0,61,62,5,
        8,0,0,62,64,3,12,6,0,63,61,1,0,0,0,64,65,1,0,0,0,65,63,1,0,0,0,65,
        66,1,0,0,0,66,11,1,0,0,0,67,68,5,9,0,0,68,69,5,2,0,0,69,73,5,11,
        0,0,70,71,5,8,0,0,71,72,5,8,0,0,72,74,3,14,7,0,73,70,1,0,0,0,74,
        75,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,13,1,0,0,0,77,78,5,1,0,
        0,78,83,5,11,0,0,79,80,5,8,0,0,80,81,5,8,0,0,81,82,5,8,0,0,82,84,
        5,9,0,0,83,79,1,0,0,0,84,85,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,
        86,92,1,0,0,0,87,88,5,9,0,0,88,89,5,2,0,0,89,90,5,10,0,0,90,92,5,
        11,0,0,91,77,1,0,0,0,91,87,1,0,0,0,92,15,1,0,0,0,93,94,5,9,0,0,94,
        95,5,2,0,0,95,96,5,10,0,0,96,97,5,11,0,0,97,17,1,0,0,0,9,21,30,34,
        42,52,65,75,85,91
    ]

class DockerComposeNetworkParser ( Parser ):

    grammarFileName = "DockerComposeNetwork.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'networks:'", "':'", "'driver'", "'attachable'", 
                     "'ipam'", "'driver_opts'", "'services:'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INDENT", "ID", "VALUE", "NEWLINE", "BLANK_LINE", 
                      "WS", "COMMENT" ]

    RULE_configFile = 0
    RULE_line = 1
    RULE_networksSection = 2
    RULE_networkDef = 3
    RULE_netProperty = 4
    RULE_servicesSection = 5
    RULE_serviceDef = 6
    RULE_serviceProperty = 7
    RULE_keyValuePair = 8

    ruleNames =  [ "configFile", "line", "networksSection", "networkDef", 
                   "netProperty", "servicesSection", "serviceDef", "serviceProperty", 
                   "keyValuePair" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    INDENT=8
    ID=9
    VALUE=10
    NEWLINE=11
    BLANK_LINE=12
    WS=13
    COMMENT=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ConfigFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DockerComposeNetworkParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerComposeNetworkParser.LineContext)
            else:
                return self.getTypedRuleContext(DockerComposeNetworkParser.LineContext,i)


        def getRuleIndex(self):
            return DockerComposeNetworkParser.RULE_configFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigFile" ):
                listener.enterConfigFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigFile" ):
                listener.exitConfigFile(self)




    def configFile(self):

        localctx = DockerComposeNetworkParser.ConfigFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_configFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4994) != 0):
                self.state = 18
                self.line()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(DockerComposeNetworkParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def networksSection(self):
            return self.getTypedRuleContext(DockerComposeNetworkParser.NetworksSectionContext,0)


        def servicesSection(self):
            return self.getTypedRuleContext(DockerComposeNetworkParser.ServicesSectionContext,0)


        def keyValuePair(self):
            return self.getTypedRuleContext(DockerComposeNetworkParser.KeyValuePairContext,0)


        def INDENT(self):
            return self.getToken(DockerComposeNetworkParser.INDENT, 0)

        def BLANK_LINE(self):
            return self.getToken(DockerComposeNetworkParser.BLANK_LINE, 0)

        def getRuleIndex(self):
            return DockerComposeNetworkParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = DockerComposeNetworkParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.networksSection()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.servicesSection()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.keyValuePair()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 29
                    self.match(DockerComposeNetworkParser.INDENT)


                self.state = 32
                self.keyValuePair()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 33
                self.match(DockerComposeNetworkParser.BLANK_LINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NetworksSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(DockerComposeNetworkParser.NEWLINE, 0)

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(DockerComposeNetworkParser.INDENT)
            else:
                return self.getToken(DockerComposeNetworkParser.INDENT, i)

        def networkDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerComposeNetworkParser.NetworkDefContext)
            else:
                return self.getTypedRuleContext(DockerComposeNetworkParser.NetworkDefContext,i)


        def getRuleIndex(self):
            return DockerComposeNetworkParser.RULE_networksSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNetworksSection" ):
                listener.enterNetworksSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNetworksSection" ):
                listener.exitNetworksSection(self)




    def networksSection(self):

        localctx = DockerComposeNetworkParser.NetworksSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_networksSection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(DockerComposeNetworkParser.T__0)
            self.state = 37
            self.match(DockerComposeNetworkParser.NEWLINE)
            self.state = 40 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 38
                    self.match(DockerComposeNetworkParser.INDENT)
                    self.state = 39
                    self.networkDef()

                else:
                    raise NoViableAltException(self)
                self.state = 42 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NetworkDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DockerComposeNetworkParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(DockerComposeNetworkParser.NEWLINE, 0)

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(DockerComposeNetworkParser.INDENT)
            else:
                return self.getToken(DockerComposeNetworkParser.INDENT, i)

        def netProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerComposeNetworkParser.NetPropertyContext)
            else:
                return self.getTypedRuleContext(DockerComposeNetworkParser.NetPropertyContext,i)


        def getRuleIndex(self):
            return DockerComposeNetworkParser.RULE_networkDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNetworkDef" ):
                listener.enterNetworkDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNetworkDef" ):
                listener.exitNetworkDef(self)




    def networkDef(self):

        localctx = DockerComposeNetworkParser.NetworkDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_networkDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(DockerComposeNetworkParser.ID)
            self.state = 45
            self.match(DockerComposeNetworkParser.T__1)
            self.state = 46
            self.match(DockerComposeNetworkParser.NEWLINE)
            self.state = 50 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 47
                    self.match(DockerComposeNetworkParser.INDENT)
                    self.state = 48
                    self.match(DockerComposeNetworkParser.INDENT)
                    self.state = 49
                    self.netProperty()

                else:
                    raise NoViableAltException(self)
                self.state = 52 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NetPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALUE(self):
            return self.getToken(DockerComposeNetworkParser.VALUE, 0)

        def NEWLINE(self):
            return self.getToken(DockerComposeNetworkParser.NEWLINE, 0)

        def ID(self):
            return self.getToken(DockerComposeNetworkParser.ID, 0)

        def getRuleIndex(self):
            return DockerComposeNetworkParser.RULE_netProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNetProperty" ):
                listener.enterNetProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNetProperty" ):
                listener.exitNetProperty(self)




    def netProperty(self):

        localctx = DockerComposeNetworkParser.NetPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_netProperty)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 632) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 55
            self.match(DockerComposeNetworkParser.T__1)
            self.state = 56
            self.match(DockerComposeNetworkParser.VALUE)
            self.state = 57
            self.match(DockerComposeNetworkParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServicesSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(DockerComposeNetworkParser.NEWLINE, 0)

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(DockerComposeNetworkParser.INDENT)
            else:
                return self.getToken(DockerComposeNetworkParser.INDENT, i)

        def serviceDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerComposeNetworkParser.ServiceDefContext)
            else:
                return self.getTypedRuleContext(DockerComposeNetworkParser.ServiceDefContext,i)


        def getRuleIndex(self):
            return DockerComposeNetworkParser.RULE_servicesSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServicesSection" ):
                listener.enterServicesSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServicesSection" ):
                listener.exitServicesSection(self)




    def servicesSection(self):

        localctx = DockerComposeNetworkParser.ServicesSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_servicesSection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(DockerComposeNetworkParser.T__6)
            self.state = 60
            self.match(DockerComposeNetworkParser.NEWLINE)
            self.state = 63 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 61
                    self.match(DockerComposeNetworkParser.INDENT)
                    self.state = 62
                    self.serviceDef()

                else:
                    raise NoViableAltException(self)
                self.state = 65 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServiceDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DockerComposeNetworkParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(DockerComposeNetworkParser.NEWLINE, 0)

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(DockerComposeNetworkParser.INDENT)
            else:
                return self.getToken(DockerComposeNetworkParser.INDENT, i)

        def serviceProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerComposeNetworkParser.ServicePropertyContext)
            else:
                return self.getTypedRuleContext(DockerComposeNetworkParser.ServicePropertyContext,i)


        def getRuleIndex(self):
            return DockerComposeNetworkParser.RULE_serviceDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServiceDef" ):
                listener.enterServiceDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServiceDef" ):
                listener.exitServiceDef(self)




    def serviceDef(self):

        localctx = DockerComposeNetworkParser.ServiceDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_serviceDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(DockerComposeNetworkParser.ID)
            self.state = 68
            self.match(DockerComposeNetworkParser.T__1)
            self.state = 69
            self.match(DockerComposeNetworkParser.NEWLINE)
            self.state = 73 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 70
                    self.match(DockerComposeNetworkParser.INDENT)
                    self.state = 71
                    self.match(DockerComposeNetworkParser.INDENT)
                    self.state = 72
                    self.serviceProperty()

                else:
                    raise NoViableAltException(self)
                self.state = 75 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServicePropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(DockerComposeNetworkParser.NEWLINE, 0)

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(DockerComposeNetworkParser.INDENT)
            else:
                return self.getToken(DockerComposeNetworkParser.INDENT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DockerComposeNetworkParser.ID)
            else:
                return self.getToken(DockerComposeNetworkParser.ID, i)

        def VALUE(self):
            return self.getToken(DockerComposeNetworkParser.VALUE, 0)

        def getRuleIndex(self):
            return DockerComposeNetworkParser.RULE_serviceProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServiceProperty" ):
                listener.enterServiceProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServiceProperty" ):
                listener.exitServiceProperty(self)




    def serviceProperty(self):

        localctx = DockerComposeNetworkParser.ServicePropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_serviceProperty)
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(DockerComposeNetworkParser.T__0)
                self.state = 78
                self.match(DockerComposeNetworkParser.NEWLINE)
                self.state = 83 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 79
                        self.match(DockerComposeNetworkParser.INDENT)
                        self.state = 80
                        self.match(DockerComposeNetworkParser.INDENT)
                        self.state = 81
                        self.match(DockerComposeNetworkParser.INDENT)
                        self.state = 82
                        self.match(DockerComposeNetworkParser.ID)

                    else:
                        raise NoViableAltException(self)
                    self.state = 85 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(DockerComposeNetworkParser.ID)
                self.state = 88
                self.match(DockerComposeNetworkParser.T__1)
                self.state = 89
                self.match(DockerComposeNetworkParser.VALUE)
                self.state = 90
                self.match(DockerComposeNetworkParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyValuePairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DockerComposeNetworkParser.ID, 0)

        def VALUE(self):
            return self.getToken(DockerComposeNetworkParser.VALUE, 0)

        def NEWLINE(self):
            return self.getToken(DockerComposeNetworkParser.NEWLINE, 0)

        def getRuleIndex(self):
            return DockerComposeNetworkParser.RULE_keyValuePair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyValuePair" ):
                listener.enterKeyValuePair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyValuePair" ):
                listener.exitKeyValuePair(self)




    def keyValuePair(self):

        localctx = DockerComposeNetworkParser.KeyValuePairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_keyValuePair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(DockerComposeNetworkParser.ID)
            self.state = 94
            self.match(DockerComposeNetworkParser.T__1)
            self.state = 95
            self.match(DockerComposeNetworkParser.VALUE)
            self.state = 96
            self.match(DockerComposeNetworkParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





