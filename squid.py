from errbot import BotPlugin, botcmd


class Squid(BotPlugin):
    """
    A plugin to identify the daily squid team member
    """

    @botcmd
    def squid_me(self, mess, args):
        """
        Assign someone to be the squid
        """
        if not args:
            assignee = mess.frm.person
        else:
            assignee = args

        self["SQUID_ASSIGNEE"] = assignee
        squid_sucker = "Have a wonderful squid day " + assignee
        return squid_sucker

    @botcmd
    def squid(self, mess, assignee):
        daily_squid = self["SQUID_ASSIGNEE"]
        squid_message = "Todays squid: " + daily_squid
        return squid_message
