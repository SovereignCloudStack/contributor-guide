==============================
License considerations for SCS
==============================

As Sovereign Cloud Stack (`SCS <https://scs.community/>`_), our mission is to provide Operators
(be it Cloud Service Providers or just internal IT departments) with a well working software
stack, that avoids exposing them to legal risks or additional restrictions that limits the
usefulness. Free software licenses have this intention but differ in how they achieve it and in
what kind of protections they provide. In the first approximation, all `OSI
<https://opensource.org/licenses>`_-approved open source licenses can be considered as valid
options. As a matter of fact, we do consider projects under such licenses as valid modules for
SCS -- where we use such projects and adjust or extend them, we would provide our contributions
under the license terms of the respective project, so we can achieve our goal to feed back code
upstream to the respective project, contribute to it and avoid fragmentation.

Where we do create independent code, we do have additional preferences, though.

For our own code, we do prefer the `Affero General Public License version 3
<https://www.gnu.org/licenses/agpl-3.0.html>`_ (AGPLv3) as license. Likewise, for documentation,
we prefer `CC-BY-SA <https://en.wikipedia.org/wiki/CC-BY-SA>`_.

Reciprocity
-----------

The GPL family of licenses are reciprocal licenses -- sometimes called `copyleft
<https://en.wikipedia.org/wiki/Copyleft>`_ licenses -- the recipient of the licensed code can
make all sorts of modifications, but if she uses the code to release software (GPL) or provide a
networked service (AGPL) to others, then she must grant the same rights to the recipients --
this includes making the modifications available under the same terms as the received software.
Microsoft has infamously `attacked
<https://web.archive.org/web/20010615205548/http://suntimes.com/output/tech/cst-fin-micro01.html>`_
copyleft licenses (and specifically the GPL) as cancerous "viral" license.

Reciprocity has many advantages:

* Code that has been created as free software will stay free. While GPL code can be
  combined in a larger software collection with proprietary software, the code itself
  including its enhancements etc. (technically: all derived works[*]_) will remain free.

* The obligation to make the changes available avoids fragmentation. As changed and
  "improved" versions need to be made available, it is much easier to review and feed
  those changes back and create a unified upstream codebase that reflects the needs of
  the complete userbase by including the needed changes. This was observed and
  `reported <https://lwn.net/Articles/660428/>`_ by Martin Fink (HP's former CTO).

The hugely successful `Linux kernel <https://kernel.org/>`_ project uses the GNU GPL;
many of the more traditional key projects in the open source world use copyleft licenses such as
the AGPL, GNU GPL, GNU LGPL or MPL.

Controversy
-----------

* Not fulfilling the license terms of a software license typically leads to the ability
  for the license owner to revoke the license -- as it is relatively easy to not fulfill
  all obligations of the GPL out of sheer negligence, the revocation without prior
  warning seems disproportionate -- this is sometimes called the GPL death penalty.
  The open source community though has a strong interest in bringing every licensee into
  compliance by giving violators a fair chance to correct their behavior. SCS explicitly
  supports the `GPL Cooperation Commitment <https://gplcc.github.io/gplcc/>`_ and pledges
  to give violators a warning and a chance to correct action by allowing for a cure period.
  This is a bit of a legacy issue -- the GPL version 3 does already contain language
  that has cure provisions.

* Many companies seem to be worried that they will inadvertently violate the GPL by negligence.
  And it is true that a company needs a tighter control of the usage of inbound source code
  which comes with a reciprocal license than the permissive BSD 3-clause or Apache Software (v2)
  licenses. This advantage however quickly turns into a disadvantage as soon as the company does
  significant outbound open source contributions under a permissive license -- they rarely want
  to give their competitors an opportunity to consume their contributions and then add
  proprietary changes to gain an advantage.  In general, companies are well advised to have a
  detailed understanding of all code that is being used and contributed and their respective
  license terms -- for proprietary and open source code and for reciprocal and for permissive
  licenses.  Some companies have successfully installed license review boards or `open source
  review boards
  <https://www.linuxfoundation.org/resources/open-source-guides/using-open-source-code/>`_ to
  create oversight, recommendations and policies to ease the governance.

Despite this, many of the recent open source projects, especially in the cloud world
have adopted permissive licenses, such as X11, BSD 3-clause, MIT and especially the popular
`Apache software license <https://en.wikipedia.org/wiki/Apache_License>`_ (ASL2), as it
appears to allow for faster adoption by companies that may not have mature open source
policies in place.


Affero
------

The reciprocity of the GNU GPL does not apply on the creation of a derived work. A company
can consume GPL'ed code and change it to their own liking without ever making any the
changes available if only used in-house. The terms however do apply as soon as the derived
work is released, i.e. the software is passed on to a third party.

In modern times, software is often used to provide a service (think SaaS) to third parties.
Unlike the standard GPL, the Affero GPL (AGPL) does consider the act of making it available in
such a way as similar to releasing the software and does require that applied changes are being
made available in this case.

The AGPL thus closes a shortcoming in the traditional non-Affero GPL.

The very successful `nextcloud <https://nextcloud.org/>`_ project uses the AGPLv3.

Patents
-------

Free software lienses are intended to give users broad rights -- the GNU GPL talks about the
`four freedoms <https://fsfe.org/freesoftware/>`_ to use software for any purpose, to study und
adjust the software (this needs source code access), to redistribute the software and to improve
it and to make these improvements available.

Software patents can significantly subvert the intended rights -- the open source community in
general dislikes software patents for this and many other reasons that are discussed
`elsewhere <https://en.wikipedia.org/wiki/Software_patents_and_free_software>`_ .
In some countries, there are rules that prevent pure software from being patented, though not
all patent offices are fully following these rules.[#]_

As software patents are existing and a serious danger to the open source goals, there are a few
attempts to improve the situation. The Apache Software License (a permissive license), requires
code contributors to grant an implicit patent license to all downstream recipients of the code
to use it in the project that it was contributed to. The
`Open Invention Network <https://www.openinventionnetwork.com/>`_ (OIN) has a
meanwhile huge patent pool that is cross-licensed between all participants and which can freely
be used by a large list of covered open source software by everyone, except for those that
raise patent violation claims against any of the covered open source projects.

Should SCS be in a position to make inventions that should be protected by a software patent,
it pledges to contribute these to the OIN pool.

Copyright Assignments
---------------------

Many software projects use `Contributor License Agreements
<https://en.wikipedia.org/wiki/Contributor_License_Agreement>`_ (CLAs), where any code
contribution needs to assign the copyright to the project owner (a foundation or sometimes a
company). This ensures that the project owner has all needed rights. It also allows the project
owner to enforce the license, to change it or to create derived works under a different license.

While this is advantageous for the project owner, it is not necessarily advantageous for the
code contributor.

Copyright enforcement does not require all copyrights to be held by a legal entity. Any holder
of significant copyrights can actually enforce it against violators.

The Linux kernel and an increasing number of projects do not work with copyright assignments but
with `Developer Certificates of Origin
<https://en.wikipedia.org/wiki/Developer_Certificate_of_Origin>`_ (DCO -- the signed-off lines
of kernel commits).  This is deemed sufficient to document the origin and the authorization to
contribute code.

The SCS project does not intend to change the license nor to create differently licensed derived
works -- it has thus decided to abstain from CLAs and use DCOs instead.

Further reading on DCO:

* https://developercertificate.org
* https://julien.ponge.org/blog/developer-certificate-of-origin-versus-contributor-license-agreements/
* https://lwn.net/Articles/592503/


.. [*] Consuming source code and binary linking is typically considered creating derived
   works, whereas interacting via a network API or starting another process is typically
   considered a copyright boundary; using Linux system calls has been explicitly called
   out to be a copyright boundary.

.. [#] https://en.wikipedia.org/wiki/Software_patents_under_the_European_Patent_Convention
